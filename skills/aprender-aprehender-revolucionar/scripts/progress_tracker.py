#!/usr/bin/env python3
"""
progress_tracker.py · MetodologIA · Aprender·Aprehender·(R)Evolucionar

Lee/actualiza .aprender-state.json con progreso en las 10 escalas de maestría.

Usage:
    python progress_tracker.py --status                   # Ver estado actual
    python progress_tracker.py --add-tema "Rust"          # Agregar tema nuevo
    python progress_tracker.py --update Rust --escala 2   # Actualizar escala
    python progress_tracker.py --add-horas Rust --horas 4
    python progress_tracker.py --export                   # Markdown summary

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any, Optional

VERSION = "1.0.0"
SKILL_DIR = Path.home() / ".claude/skills/aprender-aprehender-revolucionar"
STATE_FILE = SKILL_DIR / ".aprender-state.json"

ESCALAS = {
    0: ("Ignorante", "Unaware"),
    1: ("Curioso", "Curious"),
    2: ("Explorador", "Explorer"),
    3: ("Iniciado", "Initiate"),
    4: ("Practicante", "Practitioner"),
    5: ("Competente", "Competent"),
    6: ("Versado", "Versed"),
    7: ("Experto", "Expert"),
    8: ("Maestro", "Master"),
    9: ("Referente", "Referent"),
}


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def load_state() -> dict[str, Any]:
    if not STATE_FILE.exists():
        return {
            "version": VERSION,
            "ultima_invocacion": now_iso(),
            "javier": {
                "industria": "Consultoría · PreSales SAP/Cloud",
                "rol_actual": "PreSales Architect Sofka + Founder MetodologIA",
                "escala_objetivo_default": 3,
            },
            "temas_activos": [],
            "auditoria_mensual_ultima": None,
            "auditoria_mensual_proxima": None,
            "skills_release_pending": [],
            "rituales_activos": [],
        }
    return json.loads(STATE_FILE.read_text())


def save_state(state: dict[str, Any]) -> None:
    state["ultima_invocacion"] = now_iso()
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def find_tema(state: dict[str, Any], tema: str) -> Optional[dict[str, Any]]:
    for t in state["temas_activos"]:
        if t["tema"].lower() == tema.lower():
            return t
    return None


def cmd_status(state: dict[str, Any]) -> str:
    out = ["# Estado · Aprender·Aprehender·(R)Evolucionar", ""]
    out.append(f"**Última invocación**: {state['ultima_invocacion']}")
    out.append(f"**Industria**: {state['javier']['industria']}")
    out.append(f"**Rol**: {state['javier']['rol_actual']}")
    out.append("")
    out.append("## Temas activos")

    if not state["temas_activos"]:
        out.append("\n_No hay temas activos. Usa --add-tema para empezar._")
    else:
        out.append("")
        for t in state["temas_activos"]:
            esc_es, esc_en = ESCALAS.get(t.get("escala_actual", 0), ("?", "?"))
            obj_es, _ = ESCALAS.get(t.get("escala_objetivo", 0), ("?", "?"))
            out.append(f"### {t['tema']}")
            out.append(f"- Fase: **{t.get('fase_actual', 'aprender')}**")
            out.append(f"- Escala: **{t.get('escala_actual', 0)} {esc_es}** → objetivo **{t.get('escala_objetivo', 3)} {obj_es}**")
            out.append(f"- Horas: {t.get('horas_invertidas', 0)} / {t.get('horas_objetivo', '?')}")
            out.append(f"- Próximo gate: {t.get('proximo_gate', 'G-Aprender')}")
            if t.get("notas"):
                out.append(f"- Notas: {t['notas']}")
            out.append("")

    out.append("## Auditoría mensual")
    out.append(f"- Última: {state.get('auditoria_mensual_ultima', 'nunca')}")
    out.append(f"- Próxima: {state.get('auditoria_mensual_proxima', 'no agendada')}")

    if state.get("skills_release_pending"):
        out.append("\n## Skills pendientes de soltar")
        for s in state["skills_release_pending"]:
            out.append(f"- {s}")

    return "\n".join(out)


def cmd_add_tema(state: dict[str, Any], tema: str, objetivo: int = 3, horas_obj: int = 20) -> dict[str, Any]:
    if find_tema(state, tema):
        print(f"⚠️  Tema '{tema}' ya existe", file=sys.stderr)
        return state
    state["temas_activos"].append({
        "id": f"{tema.lower().replace(' ', '-')}-{datetime.datetime.now().strftime('%Y%m%d')}",
        "tema": tema,
        "fase_actual": "aprender",
        "escala_actual": 0,
        "escala_objetivo": objetivo,
        "horas_invertidas": 0,
        "horas_objetivo": horas_obj,
        "ultimo_kata": None,
        "ultima_evaluacion": None,
        "proximo_gate": "G-Aprender",
        "ai_evaluacion": None,
        "auto_evaluacion": None,
        "notebooklm_id": None,
        "notas": "",
        "fecha_inicio": now_iso(),
    })
    print(f"✅ Tema '{tema}' agregado · objetivo Escala {objetivo} en {horas_obj}h", file=sys.stderr)
    return state


def cmd_update(state: dict[str, Any], tema: str, **kwargs) -> dict[str, Any]:
    t = find_tema(state, tema)
    if not t:
        print(f"❌ Tema '{tema}' no encontrado", file=sys.stderr)
        return state
    for k, v in kwargs.items():
        if v is not None:
            t[k] = v
    print(f"✅ Tema '{tema}' actualizado", file=sys.stderr)
    return state


def cmd_add_horas(state: dict[str, Any], tema: str, horas: float) -> dict[str, Any]:
    t = find_tema(state, tema)
    if not t:
        print(f"❌ Tema '{tema}' no encontrado", file=sys.stderr)
        return state
    t["horas_invertidas"] = t.get("horas_invertidas", 0) + horas
    print(f"✅ {horas}h agregadas a '{tema}' · total: {t['horas_invertidas']}h", file=sys.stderr)
    return state


def cmd_export(state: dict[str, Any]) -> str:
    """Exporta estado en markdown rico para reportes."""
    return cmd_status(state)


def main():
    parser = argparse.ArgumentParser(
        description="Tracker de progreso · 10 escalas de maestría"
    )
    parser.add_argument("--status", action="store_true", help="Ver estado actual")
    parser.add_argument("--add-tema", metavar="TEMA", help="Agregar tema nuevo")
    parser.add_argument("--objetivo", type=int, default=3, help="Escala objetivo (con --add-tema)")
    parser.add_argument("--horas-obj", type=int, default=20, help="Horas objetivo (con --add-tema)")
    parser.add_argument("--update", metavar="TEMA", help="Actualizar tema existente")
    parser.add_argument("--escala", type=int, help="Nueva escala (con --update)")
    parser.add_argument("--fase", choices=["aprender", "aprehender", "revolucionar"], help="Nueva fase (con --update)")
    parser.add_argument("--gate", help="Próximo gate (con --update)")
    parser.add_argument("--notas", help="Notas (con --update)")
    parser.add_argument("--add-horas", metavar="TEMA", help="Sumar horas a un tema")
    parser.add_argument("--horas", type=float, help="Cantidad de horas (con --add-horas)")
    parser.add_argument("--export", action="store_true", help="Exportar estado completo (md)")

    args = parser.parse_args()
    state = load_state()

    if args.status:
        print(cmd_status(state))
    elif args.add_tema:
        state = cmd_add_tema(state, args.add_tema, args.objetivo, args.horas_obj)
        save_state(state)
    elif args.update:
        kwargs = {}
        if args.escala is not None:
            kwargs["escala_actual"] = args.escala
        if args.fase:
            kwargs["fase_actual"] = args.fase
        if args.gate:
            kwargs["proximo_gate"] = args.gate
        if args.notas:
            kwargs["notas"] = args.notas
        state = cmd_update(state, args.update, **kwargs)
        save_state(state)
    elif args.add_horas:
        if args.horas is None:
            print("ERROR: --horas requerido con --add-horas", file=sys.stderr)
            return 1
        state = cmd_add_horas(state, args.add_horas, args.horas)
        save_state(state)
    elif args.export:
        print(cmd_export(state))
    else:
        parser.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())
