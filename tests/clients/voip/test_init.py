import tempfile
from pathlib import Path

import pem
import pytest

from kalyke import VoIPClient


def test_initialize_with_pathlib(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=auth_key_filepath,
    )

    assert isinstance(client, VoIPClient)


def test_initialize_with_str(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=str(auth_key_filepath),
    )

    assert isinstance(client, VoIPClient)


def test_initialize_with_key_filepath(auth_key_filepath):
    cer, key = pem.parse_file(auth_key_filepath)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        cer_path = tmpdir_path / "cer.pem"
        cer_path.write_bytes(cer.as_bytes())
        key_path = tmpdir_path / "key.pem"
        key_path.write_bytes(key.as_bytes())

        client = VoIPClient(
            use_sandbox=True,
            auth_key_filepath=cer_path,
            key_filepath=key_path,
        )

        assert isinstance(client, VoIPClient)


def test_initialize_with_key_filepath_and_password(auth_key_filepath):
    cer, key = pem.parse_file(auth_key_filepath)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        cer_path = tmpdir_path / "cer.pem"
        cer_path.write_bytes(cer.as_bytes())
        key_path = tmpdir_path / "key.pem"
        key_path.write_bytes(key.as_bytes())

        client = VoIPClient(
            use_sandbox=True,
            auth_key_filepath=cer_path,
            key_filepath=key_path,
            password="password",
        )

    assert isinstance(client, VoIPClient)


def test_initialize_with_password(auth_key_filepath):
    with pytest.warns(UserWarning, match="password is ignored because key_filepath is None."):
        client = VoIPClient(
            use_sandbox=True,
            auth_key_filepath=auth_key_filepath,
            password="password",
        )

        assert isinstance(client, VoIPClient)
