import pytest

from kalyke import ApnsConfig, VoIPClient
from kalyke.exceptions import BadDeviceToken


@pytest.mark.asyncio
async def test_success(httpx_mock, auth_key_filepath):
    httpx_mock.add_response(status_code=200, http_version="HTTP/2.0", headers={"apns-id": "stub_apns_id"})

    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=auth_key_filepath,
    )
    apns_id = await client.send_message(
        device_token="stub_device_token",
        payload={"data": "test data"},
        apns_config=ApnsConfig(topic="com.example.App.voip"),
    )

    assert apns_id == "stub_apns_id"


@pytest.mark.asyncio
async def test_failure(httpx_mock, auth_key_filepath):
    httpx_mock.add_response(
        status_code=400,
        http_version="HTTP/2.0",
        json={
            "reason": "BadDeviceToken",
        },
    )

    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(BadDeviceToken) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload={"data": "test data"},
            apns_config=ApnsConfig(topic="com.example.App.voip"),
        )

    assert str(e.value) == str(BadDeviceToken(error={}))
