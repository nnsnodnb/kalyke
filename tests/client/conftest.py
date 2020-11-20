import pytest
from typing import Dict

from kalyke.client import PRODUCTION_HOST, SANDBOX_HOST


@pytest.fixture()
def mock_response() -> Dict[str, str]:
    return {"apns-id": "eabeae54-14a8-11e5-b60b-1697f925ec7b"}


@pytest.fixture()
def requests_mock_sandbox(requests_mock, mock_response) -> None:
    requests_mock.post(SANDBOX_HOST.replace(":443", ""), mock_response)
    yield


@pytest.fixture()
def requests_mock_production(requests_mock, mock_response) -> None:
    requests_mock.post(PRODUCTION_HOST.replace(":443", ""), mock_response)
    yield
