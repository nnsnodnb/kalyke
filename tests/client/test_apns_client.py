from kalyke.client import APNsClient
from kalyke.payload import Payload


def test_apns_client_send_message(mock_create_auth_key, mock_create_token, mock_get_response) -> None:
    client = APNsClient(
        team_id="team_id",
        auth_key_id="auth_key_id",
        auth_key_filepath="/path/to/AuthKey_auth_key_id.p8",
        bundle_id="moe.nnsnodnb.kalyke.test",
        use_sandbox=True,
        force_proto="h2",
    )
    alert = Payload(alert="test")
    result = client.send_message("dummy_registration_id", alert)

    assert result
