import datetime

from pathlib import Path
from unittest.mock import MagicMock

import jwt
import pytest

from kalyke import ApnsClient


def test_success(auth_key_filepath):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 1, 10, 23, 6, 34)

    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )
    token = client._make_authorization()

    expect = jwt.encode(
        payload={
            "iss": "DUMMY_TEAM_ID",
            "iat": str(int(datetime.datetime.now().timestamp())),
        },
        key=auth_key_filepath.read_text(),
        algorithm="ES256",
        headers={
            "alg": "ES256",
            "kid": "DUMMY",
        },
    )

    actual_payload = jwt.decode(jwt=token, options={"verify_signature": False})
    expect_payload = jwt.decode(jwt=expect, options={"verify_signature": False})
    assert actual_payload == expect_payload
    assert jwt.get_unverified_header(jwt=token) == jwt.get_unverified_header(jwt=expect)


def test_file_not_found_error():
    client = ApnsClient(
        use_sandbox=True, team_id="DUMMY_TEAM_ID", auth_key_id="DUMMY", auth_key_filepath=Path("/") / "no_exist.p8"
    )

    with pytest.raises(FileNotFoundError) as e:
        _ = client._make_authorization()

    assert str(e.value) == "[Errno 2] No such file or directory: '/no_exist.p8'"
