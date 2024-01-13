from httpx import AsyncClient

from kalyke import VoIPApnsConfig, VoIPClient


def test_success(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=auth_key_filepath,
    )

    actual_client = client._init_client(
        apns_config=VoIPApnsConfig(topic="com.example.App.voip"),
    )

    assert isinstance(actual_client, AsyncClient)
