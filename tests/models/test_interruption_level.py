import pytest

from kalyke import InterruptionLevel


@pytest.mark.parametrize(
    "value, expect",
    [
        ("passive", InterruptionLevel.PASSIVE),
        ("active", InterruptionLevel.ACTIVE),
        ("time-sensitive", InterruptionLevel.TIME_SENSITIVE),
        ("critical", InterruptionLevel.CRITICAL),
    ],
)
def test_success(value, expect):
    il = InterruptionLevel(value)

    assert il == expect


def test_value_error():
    with pytest.raises(ValueError) as e:
        _ = InterruptionLevel("background")

    assert str(e.value) == "'background' is not a valid InterruptionLevel"
