from httpx import AsyncClient

from kalyke import LiveActivityApnsConfig, LiveActivityClient


def test_exist_authorization_header(auth_key_filepath):
    client = LiveActivityClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )
    actual_client = client._init_client(
        apns_config=LiveActivityApnsConfig(
            topic="com.example.App.push-type.liveactivity",
        ),
    )

    assert isinstance(actual_client, AsyncClient)
    assert actual_client.headers["authorization"].startswith("bearer ey")
