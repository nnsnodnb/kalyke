from kalyke.client import APNsClient
from kalyke.payload import PayloadAlert, Payload
from random import random

import hashlib


payload_alert = PayloadAlert(title='YOUR TITLE', body='YOUR BODY')
alert = Payload(alert=payload_alert, badge=1, sound='default')

client = APNsClient(
    team_id='YOUR_TEAM_ID', auth_key_id='AUTH_KEY_ID', auth_key_filepath='/path/to/AuthKey_AUTH_KEY_ID.p8',
    bundle_id='com.example.App', use_sandbox=True, force_proto='h2'
)

# Send single push notification

registration_id = hashlib.sha256(('%.12f' % random()).encode('utf-8')).hexdigest()

result = client.send_message(registration_id, alert)

# Send multiple push notifications
registration_ids = [
    hashlib.sha256(('%.12f' % random()).encode('utf-8')).hexdigest() for _ in range(10)
]

results = client.send_bulk_message(registration_ids, alert)
