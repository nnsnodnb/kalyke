from httpx import AsyncClient

from kalyke import ApnsClient, ApnsConfig


def test_exist_authorization_header(auth_key_filepath):
    client = ApnsClient(
        use_sandbox=True, team_id="DUMMY_TEAM_ID", auth_key_id="DUMMY", auth_key_filepath=auth_key_filepath
    )
    actual_client = client._init_client(apns_config=ApnsConfig(topic="com.example.App"))

    assert isinstance(actual_client, AsyncClient)
    assert actual_client.headers["authorization"].startswith("bearer ey")
