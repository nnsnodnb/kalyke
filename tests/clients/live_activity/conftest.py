from pathlib import Path

import pytest


@pytest.fixture()
def auth_key_filepath() -> Path:
    return Path(__file__).parent.parent / "dummy.p8"
