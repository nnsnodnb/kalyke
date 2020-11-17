from kalyke.client import VoIPClient


client = VoIPClient(
    auth_key_filepath="/path/to/YOUR_VOIP_CERTIFICATE.pem", bundle_id="com.example.App.voip", use_sandbox=True
)

alert = {"key": "value"}

# Send single VoIP notification

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

result = client.send_message(registration_id, alert)

# Send multiple VoIP notifications

registration_ids = [
    "87b0a5ab7b91dce26ea2c97466f7b3b82b5dda4441003a2d8782fffd76515b73",
    "22a1b20cb67a43da4a8f006176788aa20271ac2e3ac0da0375ae3dc1db0de210",
]

results = client.send_bulk_message(registration_ids, alert)
