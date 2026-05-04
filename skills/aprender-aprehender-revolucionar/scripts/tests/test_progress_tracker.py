"""Tests · progress_tracker.py · v1.1.0.

Smoke tests para validaciones críticas del tracker.

Run: python -m pytest scripts/tests/test_progress_tracker.py -v

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA · 2026
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow import sin instalar paquete
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

from progress_tracker import (  # type: ignore
    DuplicateTemaError,
    InvalidEscalaError,
    ProgressTrackerError,
    TemaNotFoundError,
    _default_state,
    cmd_add_horas,
    cmd_add_tema,
    cmd_update,
    detect_regression,
    find_tema,
    validate_escala,
    validate_tema_name,
)


def test_default_state_structure() -> None:
    """Estado default tiene campos mínimos."""
    state = _default_state()
    assert "temas_activos" in state
    assert "javier" in state
    assert state["temas_activos"] == []


def test_validate_escala_valid() -> None:
    """Escalas 0-9 son válidas."""
    for esc in range(10):
        validate_escala(esc)  # No exception


def test_validate_escala_invalid() -> None:
    """Escala fuera de 0-9 lanza InvalidEscalaError."""
    with pytest.raises(InvalidEscalaError):
        validate_escala(-1)
    with pytest.raises(InvalidEscalaError):
        validate_escala(10)


def test_validate_tema_name_too_short() -> None:
    """Tema <2 chars rechazado."""
    with pytest.raises(ProgressTrackerError):
        validate_tema_name("R")
    with pytest.raises(ProgressTrackerError):
        validate_tema_name("")


def test_validate_tema_name_strips() -> None:
    """Tema se normaliza con strip."""
    assert validate_tema_name("  Rust  ") == "Rust"


def test_add_tema_creates_entry() -> None:
    """add_tema agrega entrada con campos correctos."""
    state = _default_state()
    state = cmd_add_tema(state, "Rust", objetivo=3, horas_obj=20)
    assert len(state["temas_activos"]) == 1
    t = state["temas_activos"][0]
    assert t["tema"] == "Rust"
    assert t["escala_objetivo"] == 3
    assert t["horas_objetivo"] == 20
    assert t["escala_actual"] == 0


def test_add_tema_duplicate_raises() -> None:
    """[CRITERIO-ACEPTACIÓN v1.1] Duplicado case-insensitive lanza DuplicateTemaError."""
    state = _default_state()
    cmd_add_tema(state, "Rust")
    with pytest.raises(DuplicateTemaError):
        cmd_add_tema(state, "rust")  # case-insensitive
    with pytest.raises(DuplicateTemaError):
        cmd_add_tema(state, "  RUST  ")


def test_find_tema_case_insensitive() -> None:
    """find_tema es case-insensitive."""
    state = _default_state()
    cmd_add_tema(state, "Rust")
    assert find_tema(state, "rust") is not None
    assert find_tema(state, "RUST") is not None
    assert find_tema(state, "Python") is None


def test_update_unknown_tema_raises() -> None:
    """update sobre tema inexistente lanza TemaNotFoundError."""
    state = _default_state()
    with pytest.raises(TemaNotFoundError):
        cmd_update(state, "NoExiste", escala_actual=2)


def test_update_invalid_escala_raises() -> None:
    """update con escala inválida lanza InvalidEscalaError."""
    state = _default_state()
    cmd_add_tema(state, "Rust")
    with pytest.raises(InvalidEscalaError):
        cmd_update(state, "Rust", escala_actual=99)


def test_detect_regression() -> None:
    """[NUEVO-APORTE v1.1] detect_regression detecta caída de escala."""
    t = {"escala_actual": 3}
    assert detect_regression(t, 2) is True  # Regresión
    assert detect_regression(t, 3) is False  # Igual
    assert detect_regression(t, 4) is False  # Avance


def test_add_horas_invalid() -> None:
    """add_horas con horas <=0 lanza error."""
    state = _default_state()
    cmd_add_tema(state, "Rust")
    with pytest.raises(ProgressTrackerError):
        cmd_add_horas(state, "Rust", 0)
    with pytest.raises(ProgressTrackerError):
        cmd_add_horas(state, "Rust", -5)


def test_add_horas_accumulates() -> None:
    """add_horas suma correctamente."""
    state = _default_state()
    cmd_add_tema(state, "Rust")
    cmd_add_horas(state, "Rust", 4)
    cmd_add_horas(state, "Rust", 6)
    t = find_tema(state, "Rust")
    assert t is not None
    assert t["horas_invertidas"] == 10
