import pytest

from kalyke import ApnsConfig
from kalyke.clients import __Client


@pytest.mark.asyncio
async def test_not_implemented_error():
    client = __Client()
    with pytest.raises(NotImplementedError) as e:
        _ = client._init_client(
            apns_config=ApnsConfig(topic="com.example.App"),
        )

    assert str(e.value) == ""
