from kalyke.client import VoIPClient
from random import random

import hashlib


client = VoIPClient(
    auth_key_filepath='/path/to/YOUR_VOIP_CERTIFICATE.pem',
    bundle_id='com.example.App.voip', use_sandbox=True
)

alert = {
    'key': 'value'
}

# Send single VoIP notification

registration_id = hashlib.sha256(('%.12f' % random()).encode('utf-8')).hexdigest()

result = client.send_message(registration_id, alert)

# Send multiple VoIP notifications

registration_ids = [
    hashlib.sha256(('%.12f' % random()).encode('utf-8')).hexdigest() for _ in range(10)
]

results = client.send_bulk_message(registration_ids, alert)
