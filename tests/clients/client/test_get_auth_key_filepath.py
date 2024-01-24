from pathlib import Path

import pytest

from kalyke.clients import __Client


@pytest.mark.parametrize(
    "auth_key_filepath",
    [
        Path(__file__).parent.parent / "dummy.p8",
        "../dummy.p8",
    ],
    ids=["Path object", "str"],
)
def test_get_auth_key_filepath(auth_key_filepath):
    client = __Client()
    client.auth_key_filepath = auth_key_filepath

    actual = client._get_auth_key_filepath()

    assert isinstance(actual, Path)
