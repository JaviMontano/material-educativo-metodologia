"""pytest config · isolated state file.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA · 2026
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture(autouse=True)
def isolated_state_file(monkeypatch: pytest.MonkeyPatch) -> Generator[Path, None, None]:
    """[NUEVO-APORTE v1.1] Aísla cada test del estado real del usuario."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp) / "test-state.json"
        monkeypatch.setenv("HOME", tmp)
        # Re-import progress_tracker para que use HOME mockeado
        yield tmp_path
