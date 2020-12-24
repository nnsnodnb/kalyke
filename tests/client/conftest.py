import uuid

import pytest
from kalyke.client import APNsClient, HTTP20Connection
from hyper.http20.response import HTTP20Response


@pytest.fixture()
def mock_create_auth_key(mocker) -> None:
    mocked = mocker.Mock(return_value="dummy_auth_key_secret")
    mocker.patch.object(APNsClient, "_create_auth_key", mocked)
    yield
    assert mocked.called


@pytest.fixture()
def mock_create_token(mocker) -> None:
    mocked = mocker.Mock(return_value="dummy_jwt_token")
    mocker.patch.object(APNsClient, "_create_token", mocked)
    yield
    assert mocked.called


@pytest.fixture()
def mock_get_response(mocker) -> None:
    mocked = mocker.Mock(
        return_value=HTTP20Response(headers={b":status": ("200",), b":apns-id": (str(uuid.uuid4()))}, stream="stream")
    )
    mocker.patch.object(HTTP20Connection, "get_response", mocked)
    yield
    assert mocked.called
