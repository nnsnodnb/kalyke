import asyncio

from kalyke import ApnsClient, ApnsConfig, Payload, PayloadAlert

client = ApnsClient(
    use_sandbox=True,
    team_id="YOUR_TEAM_ID",
    auth_key_id="AUTH_KEY_ID",
    auth_key_filepath="/path/to/AuthKey_AUTH_KEY_ID.p8",
)

# Send single push notification

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

payload_alert = PayloadAlert(title="YOUR TITLE", body="YOUR BODY")
payload = Payload(alert=payload_alert, badge=1, sound="default")
config = ApnsConfig(topic="com.example.App")

asyncio.run(client.send_message(device_token=registration_id, payload=payload, apns_config=config))

# Send multiple push notifications
registration_ids = [
    "87b0a5ab7b91dce26ea2c97466f7b3b82b5dda4441003a2d8782fffd76515b73",
    "22a1b20cb67a43da4a8f006176788aa20271ac2e3ac0da0375ae3dc1db0de210",
]

# results = client.send_bulk_message(registration_ids, alert)
