# kalyke

![Test](https://github.com/nnsnodnb/kalyke/workflows/Test/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/fb85bcf746e1f4025afa/maintainability)](https://codeclimate.com/github/nnsnodnb/kalyke/maintainability)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/nnsnodnb/kalyke/graph/badge.svg)](https://codecov.io/gh/nnsnodnb/kalyke)

[![PyPI Package version](https://badge.fury.io/py/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![Python Supported versions](https://img.shields.io/pypi/pyversions/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![wheel](https://img.shields.io/pypi/wheel/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![format](https://img.shields.io/pypi/format/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![implementation](https://img.shields.io/pypi/implementation/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)
[![LICENSE](https://img.shields.io/pypi/l/kalyke-apns.svg)](https://pypi.org/project/kalyke-apns)

A library for interacting with APNs and VoIP using HTTP/2.

## Installation

kalyke requires python 3.10 or later.

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

asyncio.run(
    client.send_message(
        device_token=registration_id,
        payload=payload,
        apns_config=config,
    )
)
```

### LiveActivity

> [!NOTE]
> - The topic suffix must be `.push-type.liveactivity`.
> - `LiveActivityPayload.event` default value is `LiveActivityEvent.UPDATE`.

```python
import asyncio
from datetime import datetime

from kalyke import LiveActivityClient, LiveActivityApnsConfig, LiveActivityEvent, LiveActivityPayload, PayloadAlert

client = LiveActivityClient(
    use_sandbox=True,
    team_id="YOUR_TEAM_ID",
    auth_key_id="AUTH_KEY_ID",
    auth_key_filepath="/path/to/AuthKey_AUTH_KEY_ID.p8",
)

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

payload_alert = PayloadAlert(title="YOUR TITLE", body="YOUR BODY")
payload = LiveActivityPayload(
    alert=payload_alert,
    badge=1,
    sound="default",
    timestamp=datetime.now(),
    event=LiveActivityEvent.UPDATE,
    content_state={
        "currentHealthLevel": 100,
        "eventDescription": "Adventure has begun!",
    },
)
config = LiveActivityApnsConfig(
    topic="com.example.App.push-type.liveactivity",
)

asyncio.run(
    client.send_message(
        device_token=registration_id,
        payload=payload,
        apns_config=config,
    )
)
```

### VoIP

> [!NOTE]
> - The topic suffix must be `.voip`.

```python
import asyncio
from pathlib import Path

from kalyke import VoIPApnsConfig, VoIPClient

client = VoIPClient(
    use_sandbox=True,
    auth_key_filepath=Path("/") / "path" / "to" / "YOUR_VOIP_CERTIFICATE.pem",
)

registration_id = "a8a799ba6c21e0795b07b577b562b8537418570c0fb8f7a64dca5a86a5a3b500"

payload = {"key": "value"}
config = VoIPApnsConfig(
    topic="com.example.App.voip",
)

asyncio.run(
    client.send_message(
        device_token=registration_id,
        payload=payload,
        apns_config=config,
    )
)
```

## License

This software is licensed under the MIT License (See [LICENSE](LICENSE)).
