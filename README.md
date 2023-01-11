# kalyke

![Test](https://github.com/nnsnodnb/kalyke/workflows/Test/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/fb85bcf746e1f4025afa/maintainability)](https://codeclimate.com/github/nnsnodnb/kalyke/maintainability)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/nnsnodnb/kalyke/badge.svg?branch=main)](https://coveralls.io/github/nnsnodnb/kalyke?branch=main)

[![PyPI Package version](https://badge.fury.io/py/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![Python Supported versions](https://img.shields.io/pypi/pyversions/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![wheel](https://img.shields.io/pypi/wheel/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![format](https://img.shields.io/pypi/format/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![implementation](https://img.shields.io/pypi/implementation/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![LICENSE](https://img.shields.io/pypi/l/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)

A library for interacting with APNs and VoIP using HTTP/2.

## Installation

kalyke requires python 3.7 or later.

```bash
$ pip install kalyke-apns
```

## Usage

### APNs

```python
import asyncio

from kalyke import ApnsClient, ApnsConfig, Payload, PayloadAlert

client = ApnsClient(
    use_sandbox=True,
    team_id="YOUR_TEAM_ID",
    auth_key_id="AUTH_KEY_ID",
    auth_key_filepath="/path/to/AuthKey_AUTH_KEY_ID.p8",
)

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

payload_alert = PayloadAlert(title="YOUR TITLE", body="YOUR BODY")
payload = Payload(alert=payload_alert, badge=1, sound="default")
config = ApnsConfig(topic="com.example.App")

asyncio.run(client.send_message(device_token=registration_id, payload=payload, apns_config=config))
```

### VoIP

```python
import asyncio
from pathlib import Path

from kalyke import ApnsConfig, ApnsPushType, VoIPClient

client = VoIPClient(
    use_sandbox=True,
    auth_key_filepath=Path("/") / "path" / "to" / "YOUR_VOIP_CERTIFICATE.pem",
)

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

payload = {"key": "value"}
config = ApnsConfig(topic="com.example.App.voip", push_type=ApnsPushType.VOIP)

asyncio.run(client.send_message(device_token=registration_id, payload=payload, apns_config=config))
```

## License

This software is licensed under the MIT License (See [LICENSE](LICENSE)).
