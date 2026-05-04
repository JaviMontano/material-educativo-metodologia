"""Tests · desatraso_planner.py · v1.1.0.

Smoke tests para validar generación de planes y audit de coherencia.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from desatraso_planner import (  # type: ignore
    MODES,
    plan_express,
    plan_marathon,
    plan_sprint,
)


def test_modes_table() -> None:
    """[CRITERIO-ACEPTACIÓN] Los 3 modos están definidos."""
    assert "4h" in MODES
    assert "20h" in MODES
    assert "64h" in MODES
    assert MODES["4h"]["objetivo_escala"] == 1
    assert MODES["20h"]["objetivo_escala"] == 2
    assert MODES["64h"]["objetivo_escala"] == 3


def test_plan_express_contains_workflow_1() -> None:
    """Plan Express menciona Workflow 1."""
    plan = plan_express("Rust", 0, datetime.date(2026, 5, 4))
    assert "Workflow 1" in plan
    assert "Rust" in plan
    assert "4 horas" in plan
    assert "Escala objetivo: 1" in plan


def test_plan_sprint_contains_workflow_2() -> None:
    """Plan Sprint menciona Workflow 2 + 4 semanas."""
    plan = plan_sprint("Kubernetes", 1, datetime.date(2026, 5, 4))
    assert "Workflow 2" in plan
    assert "Kubernetes" in plan
    assert "20 horas" in plan
    assert "Semana 1" in plan
    assert "Semana 4" in plan


def test_plan_marathon_contains_16_weeks() -> None:
    """Plan Marathon cubre 16 semanas."""
    plan = plan_marathon("System Design", 2, datetime.date(2026, 5, 4))
    assert "Marathon" in plan
    assert "16 semanas" in plan
    assert "Semanas 5-12" in plan
    assert "Semanas 13-16" in plan


def test_plan_express_includes_date() -> None:
    """Plan incluye fecha."""
    hoy = datetime.date(2026, 5, 4)
    plan = plan_express("Rust", 0, hoy)
    assert "2026-05-04" in plan
