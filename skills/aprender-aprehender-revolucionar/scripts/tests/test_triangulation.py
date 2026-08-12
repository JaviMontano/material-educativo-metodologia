"""Pruebas del comparador de modelos · MetodologIA v1.2."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from triangulation import triangulacion  # type: ignore


def test_model_agreement_is_not_external_confirmation(tmp_path: Path) -> None:
    paths = []
    for name in ("modelo-a", "modelo-b", "modelo-c"):
        path = tmp_path / f"{name}.md"
        path.write_text("- La afirmación aparece aquí\n", encoding="utf-8")
        paths.append(path)
    result = triangulacion(paths)
    assert "ACUERDO DE MODELOS" in result
    assert "verificar fuente" in result
    assert "alta probabilidad de verdad" not in result
