import pytest

from kalyke import ApnsClient, ApnsConfig


@pytest.mark.asyncio
async def test_success(httpx_mock, auth_key_filepath):
    httpx_mock.add_response(
        status_code=200,
        http_version="HTTP/2.0",
        headers={
            "apns-id": "stub-apns-id",
        },
        json={},
    )

    client = ApnsClient(
        use_sandbox=True, team_id="DUMMY_TEAM", auth_key_id="DUMMY", auth_key_filepath=auth_key_filepath
    )
    apns_id = await client.send_message(
        device_token="stub_device_token",
        payload={
            "alert": "test alert",
        },
        apns_config=ApnsConfig(topic="com.example.App"),
    )

    assert apns_id == "stub-apns-id"
