from httpx2 import AsyncClient

from kalyke import VoIPApnsConfig, VoIPClient


def test_exist_authorization_header(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )
    actual_client = client._init_client(
        apns_config=VoIPApnsConfig(topic="com.example.App.voip"),
    )

    assert isinstance(actual_client, AsyncClient)
    assert actual_client.headers["authorization"].startswith("bearer ey")
