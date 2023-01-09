import pytest

from kalyke import ApnsConfig
from kalyke.clients import __Client


@pytest.mark.asyncio
async def test_not_implemented_error():
    client = __Client()
    with pytest.raises(NotImplementedError) as e:
        _ = await client.send_message(
            device_token="stub_device_token",
            payload={},
            apns_config=ApnsConfig(topic="com.example.App"),
        )

    assert str(e.value) == ""
