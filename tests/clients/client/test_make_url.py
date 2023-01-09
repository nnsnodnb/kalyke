import pytest

from kalyke.clients import __Client


@pytest.mark.parametrize(
    "use_sandbox, expect",
    [
        (
            True,
            "https://api.sandbox.push.apple.com/3/device/stub_device_token",
        ),
        (
            False,
            "https://api.push.apple.com/3/device/stub_device_token",
        ),
    ],
)
def test_make_url(use_sandbox, expect):
    client = __Client()
    client.use_sandbox = use_sandbox
    url = client._make_url(device_token="stub_device_token")

    assert url == expect


def test_attribute_error():
    client = __Client()
    with pytest.raises(AttributeError) as e:
        _ = client._make_url(device_token="stub_device_token")

    assert str(e.value) == "'__Client' object has no attribute 'use_sandbox'"
