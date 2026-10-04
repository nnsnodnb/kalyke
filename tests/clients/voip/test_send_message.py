import pytest

from kalyke import ApnsConfig, VoIPApnsConfig, VoIPClient
from kalyke.exceptions import BadDeviceToken


@pytest.mark.asyncio
async def test_success(httpx2_mock, auth_key_filepath):
    httpx2_mock.add_response(
        status_code=200,
        http_version="HTTP/2.0",
        headers={
            "apns-id": "stub_apns_id",
        },
        json={},
    )

    client = VoIPClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )
    apns_id = await client.send_message(
        device_token="stub_device_token",
        payload={"data": "test data"},
        apns_config=VoIPApnsConfig(
            topic="com.example.App.voip",
        ),
    )

    assert apns_id == "stub_apns_id"


@pytest.mark.asyncio
async def test_bad_device_token(httpx2_mock, auth_key_filepath):
    httpx2_mock.add_response(
        status_code=400,
        http_version="HTTP/2.0",
        json={
            "reason": "BadDeviceToken",
        },
    )

    client = VoIPClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(BadDeviceToken) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload={
                "data": "test data",
            },
            apns_config=VoIPApnsConfig(
                topic="com.example.App.voip",
            ),
        )

    assert str(e.value) == str(BadDeviceToken(error={}))


@pytest.mark.asyncio
async def test_value_error(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(ValueError) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload=["test alert"],
            apns_config=ApnsConfig(topic="com.example.App"),
        )

    assert str(e.value) == "Type of 'payload' must be specified by Payload or Dict[str, Any]."


@pytest.mark.asyncio
async def test_invalid_topic(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    with pytest.raises(ValueError) as e:
        await client.send_message(
            device_token="stub_device_token",
            payload={"data": "test data"},
            apns_config=VoIPApnsConfig(topic="com.example.App"),
        )

    assert str(e.value) == "topic must end with .voip, but com.example.App."
