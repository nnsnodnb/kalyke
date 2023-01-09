import pytest

from kalyke.clients import __Client


@pytest.mark.parametrize(
    "use_sandbox, expect",
    [
        (True, "https://api.sandbox.push.apple.com"),
        (False, "https://api.push.apple.com"),
    ],
)
def test_base_url(use_sandbox, expect):
    client = __Client()
    client.use_sandbox = use_sandbox

    assert client._base_url == expect
