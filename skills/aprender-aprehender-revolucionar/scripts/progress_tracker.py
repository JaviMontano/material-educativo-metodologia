#!/usr/bin/env python3
"""progress_tracker.py · MetodologIA · Aprender·Aprehender·(R)Evolucionar · v1.1.0.

Lee/actualiza .aprender-state.json con progreso en las 10 escalas de maestría.

Usage:
    python progress_tracker.py --status                   # Ver estado actual
    python progress_tracker.py --add-tema "Rust"          # Agregar tema nuevo
    python progress_tracker.py --update Rust --escala 2   # Actualizar escala
    python progress_tracker.py --add-horas Rust --horas 4 # Sumar horas
    python progress_tracker.py --export                   # Markdown summary

[FUENTE-PRIMARIA] Playbook v2.0.0 §10 Escalas de Maestría.
[LÍMITE] No detecta duplicados semánticos (e.g., "Rust" vs "Rust Lang"). Coincidencia case-insensitive solo.
[SUPUESTO] Usuario provee tema canónico · escala objetivo realista (típicamente 3 para Workflow 3).
[LÍMITE] No genera el plan de acción · solo persiste estado · combinar con desatraso_planner.py.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

VERSION = "1.1.0"
SKILL_DIR = Path.home() / ".claude/skills/aprender-aprehender-revolucionar"
STATE_FILE = SKILL_DIR / ".aprender-state.json"

ESCALAS: dict[int, tuple[str, str]] = {
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

VALID_FASES = ("aprender", "aprehender", "revolucionar")
VALID_GATES = ("G-Aprender", "G-Aprehender", "G-Revolucionar")


# ============================================================
# Custom exceptions · v1.1
# ============================================================


class ProgressTrackerError(Exception):
    """[NUEVO-APORTE] Base exception class for tracker errors."""


class DuplicateTemaError(ProgressTrackerError):
    """Tema ya existe en estado."""


class TemaNotFoundError(ProgressTrackerError):
    """Tema no existe."""


class InvalidEscalaError(ProgressTrackerError):
    """Escala fuera de rango 0-9."""


class RegressionWarning(ProgressTrackerError):
    """[NUEVO-APORTE] Detectada regresión de escala (X → X-N)."""


# ============================================================
# State I/O
# ============================================================


def now_iso() -> str:
    """ISO timestamp en UTC."""
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load_state() -> dict[str, Any]:
    """Carga estado desde STATE_FILE · crea estado default si no existe."""
    if not STATE_FILE.exists():
        return _default_state()
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ProgressTrackerError(
            f"Estado corrupto en {STATE_FILE}: {e}. "
            f"Backup manual y reinicia con --status."
        ) from e


def _default_state() -> dict[str, Any]:
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


def save_state(state: dict[str, Any]) -> None:
    """Persiste estado · valida estructura mínima · ascii-safe."""
    if "temas_activos" not in state:
        raise ProgressTrackerError("Estado inválido · falta 'temas_activos'")
    state["ultima_invocacion"] = now_iso()
    state["version"] = VERSION
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def find_tema(state: dict[str, Any], tema: str) -> dict[str, Any] | None:
    """Búsqueda case-insensitive · [LÍMITE] no detecta duplicados semánticos."""
    norm = tema.strip().lower()
    for t in state["temas_activos"]:
        if t["tema"].strip().lower() == norm:
            return t
    return None


# ============================================================
# Validations · v1.1
# ============================================================


def validate_escala(escala: int) -> None:
    """[CRITERIO-ACEPTACIÓN] Escala debe estar en rango 0-9."""
    if not 0 <= escala <= 9:
        raise InvalidEscalaError(
            f"Escala {escala} fuera de rango · debe ser 0-9 (ver references/03)"
        )


def validate_tema_name(tema: str) -> str:
    """Normaliza · valida longitud mínima."""
    norm = tema.strip()
    if len(norm) < 2:
        raise ProgressTrackerError(
            f"Tema debe tener ≥2 caracteres · recibido: '{tema}'"
        )
    return norm


def detect_regression(t: dict[str, Any], new_escala: int) -> bool:
    """[NUEVO-APORTE] Detecta regresión · escala baja en >0."""
    current = t.get("escala_actual", 0)
    return new_escala < current


# ============================================================
# Commands
# ============================================================


def cmd_status(state: dict[str, Any]) -> str:
    """Markdown summary del estado actual."""
    out: list[str] = ["# Estado · Aprender·Aprehender·(R)Evolucionar", ""]
    out.append(f"**Versión skill**: {state.get('version', '?')}")
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
            esc_es, _ = ESCALAS.get(t.get("escala_actual", 0), ("?", "?"))
            obj_es, _ = ESCALAS.get(t.get("escala_objetivo", 0), ("?", "?"))
            out.append(f"### {t['tema']}")
            out.append(f"- Fase: **{t.get('fase_actual', 'aprender')}**")
            out.append(
                f"- Escala: **{t.get('escala_actual', 0)} {esc_es}** "
                f"→ objetivo **{t.get('escala_objetivo', 3)} {obj_es}**"
            )
            out.append(
                f"- Horas: {t.get('horas_invertidas', 0)} / {t.get('horas_objetivo', '?')}"
            )
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


def cmd_add_tema(
    state: dict[str, Any],
    tema: str,
    objetivo: int = 3,
    horas_obj: int = 20,
) -> dict[str, Any]:
    """Agrega tema · valida unicidad case-insensitive."""
    tema = validate_tema_name(tema)
    validate_escala(objetivo)
    if find_tema(state, tema):
        raise DuplicateTemaError(
            f"Tema '{tema}' ya existe · usa --update para modificarlo"
        )
    slug = f"{tema.lower().replace(' ', '-')}-{dt.datetime.now().strftime('%Y%m%d')}"
    state["temas_activos"].append(
        {
            "id": slug,
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
        }
    )
    print(
        f"✅ Tema '{tema}' agregado · objetivo Escala {objetivo} en {horas_obj}h",
        file=sys.stderr,
    )
    return state


def cmd_update(
    state: dict[str, Any], tema: str, **kwargs: Any
) -> dict[str, Any]:
    """Actualiza tema · detecta regresión de escala."""
    t = find_tema(state, tema)
    if not t:
        raise TemaNotFoundError(f"Tema '{tema}' no existe · usa --add-tema primero")
    if (new_escala := kwargs.get("escala_actual")) is not None:
        validate_escala(new_escala)
        if detect_regression(t, new_escala):
            print(
                f"⚠️  Regresión detectada · {t['tema']}: "
                f"{t.get('escala_actual', 0)} → {new_escala}. "
                f"¿Es intencional? Si no, revisar antes de save.",
                file=sys.stderr,
            )
    if (fase := kwargs.get("fase_actual")) is not None and fase not in VALID_FASES:
        raise ProgressTrackerError(
            f"Fase inválida '{fase}' · debe ser {VALID_FASES}"
        )
    for k, v in kwargs.items():
        if v is not None:
            t[k] = v
    print(f"✅ Tema '{tema}' actualizado", file=sys.stderr)
    return state


def cmd_add_horas(
    state: dict[str, Any], tema: str, horas: float
) -> dict[str, Any]:
    """Suma horas · valida positivo."""
    if horas <= 0:
        raise ProgressTrackerError(f"Horas deben ser >0 · recibido: {horas}")
    t = find_tema(state, tema)
    if not t:
        raise TemaNotFoundError(f"Tema '{tema}' no existe")
    t["horas_invertidas"] = t.get("horas_invertidas", 0) + horas
    print(
        f"✅ {horas}h agregadas a '{tema}' · total: {t['horas_invertidas']}h",
        file=sys.stderr,
    )
    return state


def cmd_export(state: dict[str, Any]) -> str:
    """Exporta estado en markdown rico para reportes."""
    return cmd_status(state)


# ============================================================
# CLI entry point
# ============================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Tracker de progreso · 10 escalas de maestría · v" + VERSION
    )
    parser.add_argument("--status", action="store_true", help="Ver estado actual")
    parser.add_argument("--add-tema", metavar="TEMA", help="Agregar tema nuevo")
    parser.add_argument(
        "--objetivo", type=int, default=3, help="Escala objetivo (con --add-tema)"
    )
    parser.add_argument(
        "--horas-obj", type=int, default=20, help="Horas objetivo (con --add-tema)"
    )
    parser.add_argument("--update", metavar="TEMA", help="Actualizar tema existente")
    parser.add_argument("--escala", type=int, help="Nueva escala 0-9 (con --update)")
    parser.add_argument(
        "--fase", choices=VALID_FASES, help="Nueva fase (con --update)"
    )
    parser.add_argument("--gate", help="Próximo gate (con --update)")
    parser.add_argument("--notas", help="Notas (con --update)")
    parser.add_argument("--add-horas", metavar="TEMA", help="Sumar horas a un tema")
    parser.add_argument(
        "--horas", type=float, help="Cantidad de horas (con --add-horas)"
    )
    parser.add_argument(
        "--export", action="store_true", help="Exportar estado completo (md)"
    )

    args = parser.parse_args()

    try:
        state = load_state()

        if args.status:
            print(cmd_status(state))
        elif args.add_tema:
            state = cmd_add_tema(
                state, args.add_tema, args.objetivo, args.horas_obj
            )
            save_state(state)
        elif args.update:
            kwargs: dict[str, Any] = {}
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
    except ProgressTrackerError as e:
        print(f"❌ {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n⏹  Cancelado por usuario", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
