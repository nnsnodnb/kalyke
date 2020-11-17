# kalyke

![Test](https://github.com/nnsnodnb/kalyke/workflows/Test/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/fb85bcf746e1f4025afa/maintainability)](https://codeclimate.com/github/nnsnodnb/kalyke/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9551aa9ca66a47a787e0db53068382b0)](https://app.codacy.com/app/nnsnodnb/kalyke?utm_source=github.com&utm_medium=referral&utm_content=nnsnodnb/kalyke&utm_campaign=Badge_Grade_Dashboard)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![PyPI Package version](https://badge.fury.io/py/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![Python Supported versions](https://img.shields.io/pypi/pyversions/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![PyPI status](https://img.shields.io/pypi/status/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![wheel](https://img.shields.io/pypi/wheel/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![format](https://img.shields.io/pypi/format/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![implementation](https://img.shields.io/pypi/implementation/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![LICENSE](https://img.shields.io/pypi/l/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)

A library for interacting with APNs and VoIP using HTTP/2.

## Installation

kalyke requires python 3.6 or later.

```bash
$ pip install kalyke-apns
```

## Usage

### APNs

```python
from kalyke.client import APNsClient
from kalyke.payload import PayloadAlert, Payload


payload_alert = PayloadAlert(title="YOUR TITLE", body="YOUR BODY")
alert = Payload(alert=payload_alert, badge=1, sound="default")

client = APNsClient(
    team_id="YOUR_TEAM_ID", auth_key_id="AUTH_KEY_ID", auth_key_filepath="/path/to/AuthKey_AUTH_KEY_ID.p8",
    bundle_id="com.example.App", use_sandbox=True, force_proto="h2"
)
# or background push
"""
client = APNsClient(
    team_id="YOUR_TEAM_ID", auth_key_id="AUTH_KEY_ID", auth_key_filepath="/path/to/AuthKey_AUTH_KEY_ID.p8",
    bundle_id="com.example.App", use_sandbox=True, force_proto="h2", apns_push_type="background"
)
"""

# Send single push notification

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

result = client.send_message(registration_id, alert)

# Send multiple push notifications
registration_ids = [
    "87b0a5ab7b91dce26ea2c97466f7b3b82b5dda4441003a2d8782fffd76515b73",
    "22a1b20cb67a43da4a8f006176788aa20271ac2e3ac0da0375ae3dc1db0de210"
]

results = client.send_bulk_message(registration_ids, alert)
```

### VoIP

```python
from kalyke.client import VoIPClient


client = VoIPClient(
    auth_key_filepath="/path/to/YOUR_VOIP_CERTIFICATE.pem",
    bundle_id="com.example.App.voip", use_sandbox=True
)

alert = {
    "key": "value"
}

# Send single VoIP notification

registration_id = "14924adeeabaacc8b38cfd766965abffd0ee572a5a89e7ee26e6009a3f1a8e8a"

result = client.send_message(registration_id, alert)

# Send multiple VoIP notifications

registration_ids = [
    "84b7120bf190d171ff904bc943455d6081274714b32c486fa28814be7ee921fb",
    "afaa8dcedc99d420e35f7435edad4821dbad3c8c7d5071b2697da9bd7a5037ad"
]

results = client.send_bulk_message(registration_ids, alert)
```

## Todo

- [ ] Tests

## License

This software is licensed under the MIT License (See [LICENSE](LICENSE)).
