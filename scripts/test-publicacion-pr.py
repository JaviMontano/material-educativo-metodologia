#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


EXPECTED = [
    "index.html",
    "README.md",
    "CHANGELOG.md",
    "docs/inventario-publicacion-canon-2026-05-20.md",
    "biblioteca/index.html",
    "prompting-universal/index.html",
    "programa-empoderamiento/index.html",
    "claude-jarvis/index.html",
    "cartillas-ia/index.html",
    "estudio/index.html",
    "claude-jarvis/ejercicio-clase-jarvis-os-en-claude.html",
    "ejercicio-clase-jarvis-os-en-claude.html",
    "claude-jarvis/scaffolding-base/index.html",
    "claude-jarvis/scaffolding-base/01_Estaciones/Contexto Profesional/index.html",
]

SENSITIVE = [
    "/Users/deonto/",
    "00_Recursos/informacion-personal",
    "memory/personas/personales",
]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.titles = 0
        self.details = 0
        self.copy_buttons = 0
        self.cards = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k: (v or "") for k, v in attrs}
        if "id" in data:
            self.ids.append(data["id"])
        if "href" in data:
            self.hrefs.append(data["href"])
        if tag == "title":
            self.titles += 1
        if tag == "details" and "prompt-layer" in data.get("class", ""):
            self.details += 1
        if "data-copy" in data:
            self.copy_buttons += 1
        if "card" in data.get("class", "").split():
            self.cards += 1


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout.strip()


def check_link(root: Path, source: Path, href: str) -> bool:
    if href.startswith(("http:", "https:", "mailto:", "#")):
        return True
    clean = href.split("#", 1)[0]
    if not clean:
        return True
    target = source.parent / clean
    if href.endswith("/"):
        target = target / "index.html"
    return target.exists()


def main() -> int:
    ap = argparse.ArgumentParser(description="Regression checks for PR #4 publicacion canon.")
    ap.add_argument("--root", default=".", help="material-educativo-metodologia root")
    ap.add_argument("--out", default=None, help="output directory")
    ap.add_argument("--pr", default="4", help="GitHub PR number")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    out = Path(args.out).resolve() if args.out else root / ".validation" / "test-runs" / datetime.now().strftime("%Y%m%d-%H%M%S")
    out.mkdir(parents=True, exist_ok=True)

    checks: list[dict[str, str]] = []

    def add(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"name": name, "status": "pass" if ok else "fail", "detail": detail})

    for rel in EXPECTED:
        add(f"exists:{rel}", (root / rel).exists(), str(root / rel))

    code, output = run([sys.executable, "scripts/validate-publicacion-canon.py"], root)
    add("validate_publicacion_canon", code == 0, output)

    code, output = run(["gh", "pr", "view", args.pr, "--repo", "JaviMontano/material-educativo-metodologia", "--json", "state,headRefName,baseRefName,url"], root)
    if code == 0:
        data = json.loads(output)
        add("github_pr_open", data.get("state") == "OPEN", output)
        add("github_pr_branch", data.get("headRefName") == "feat/publicacion-material-educativo-canon-2026-05-20" and data.get("baseRefName") == "main", output)
    else:
        add("github_pr_view", False, output)

    prompt_data = json.loads((root / "prompts_universales_v3000.json").read_text(encoding="utf-8"))
    prompts = prompt_data.get("prompts", [])
    ids = [p.get("id") for p in prompts]
    invokes: list[str] = []
    for item in prompts:
        val = item.get("invoke", [])
        invokes.extend(val if isinstance(val, list) else [val])
    add("json_total_2026", prompt_data.get("total") == 2026 and prompt_data.get("cap") == 2026 and len(prompts) == 2026, f"total={prompt_data.get('total')} cap={prompt_data.get('cap')} prompts={len(prompts)}")
    add("json_unique_ids", len(ids) == len(set(ids)), f"ids={len(ids)} unique={len(set(ids))}")
    add("json_unique_invokes", len(invokes) == len(set(invokes)), f"invokes={len(invokes)} unique={len(set(invokes))}")
    prompster = json.loads((root / "prompts_universales_v2026_prompster.json").read_text(encoding="utf-8"))
    add("prompster_2026_entries", isinstance(prompster, dict) and len(prompster) == 2026, f"entries={len(prompster) if isinstance(prompster, dict) else 'not-dict'}")

    for rel in [x for x in EXPECTED if x.endswith(".html")]:
        path = root / rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        parser = Parser()
        parser.feed(text)
        add(f"title:{rel}", parser.titles > 0, f"titles={parser.titles}")
        add(f"unique_ids:{rel}", len(parser.ids) == len(set(parser.ids)), f"ids={len(parser.ids)} unique={len(set(parser.ids))}")
        broken = [href for href in parser.hrefs if not check_link(root, path, href)]
        add(f"links:{rel}", not broken, ", ".join(broken[:8]))
        add(f"no_sensitive_paths:{rel}", not any(x in text for x in SENSITIVE), "local/privacy path markers")
        if "ejercicio-clase" in rel:
            add(f"exercise_contract:{rel}", parser.details == 12 and parser.copy_buttons == 16, f"details={parser.details} copy={parser.copy_buttons}")

    failures = [c for c in checks if c["status"] != "pass"]
    payload = {"status": "fail" if failures else "pass", "generated_at": datetime.now().isoformat(timespec="seconds"), "checks": checks}
    (out / "publicacion-pr-report.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Publicacion PR regression", "", f"Status: **{payload['status'].upper()}**", ""]
    lines.extend(f"- `{c['status']}` · **{c['name']}**" + (f" · {c['detail']}" if c["detail"] else "") for c in checks)
    (out / "report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"publicacion_pr_report={out / 'report.md'}")
    if failures:
        print(f"publicacion_pr_failures={len(failures)}")
        return 1
    print("publicacion_pr_ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
