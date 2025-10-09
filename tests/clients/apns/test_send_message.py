import pytest

from kalyke import ApnsClient, ApnsConfig, Payload
from kalyke.exceptions import BadDeviceToken


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "payload",
    [
        Payload(alert="test alert"),
        {"alert": "test alert"},
    ],
    ids=["Payload object", "dict"],
)
async def test_success(httpx_mock, auth_key_filepath, payload):
    httpx_mock.add_response(
        status_code=200,
        http_version="HTTP/2.0",
        headers={
            "apns-id": "stub-apns-id",
        },
        json={},
    )

    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )
    apns_id = await client.send_message(
        device_token="stub_device_token",
        payload=payload,
        apns_config=ApnsConfig(
            topic="com.example.App",
        ),
    )

    assert apns_id == "stub-apns-id"


@pytest.mark.asyncio
async def test_bad_device_token(httpx_mock, auth_key_filepath):
    httpx_mock.add_response(
        status_code=400,
        http_version="HTTP/2.0",
        json={
            "reason": "BadDeviceToken",
        },
    )

    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(BadDeviceToken) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload={
                "alert": "test alert",
            },
            apns_config=ApnsConfig(
                topic="com.example.App",
            ),
        )

    assert str(e.value) == str(BadDeviceToken(error={}))


@pytest.mark.asyncio
async def test_value_error(httpx_mock, auth_key_filepath):
    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(ValueError) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload=["test alert"],
            apns_config=ApnsConfig(
                topic="com.example.App",
            ),
        )

    assert str(e.value) == "Type of 'payload' must be specified by Payload or Dict[str, Any]."
