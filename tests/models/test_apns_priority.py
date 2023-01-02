import pytest

from kalyke import ApnsPriority


@pytest.mark.parametrize(
    "value, expect",
    [
        (10, ApnsPriority.IMMEDIATELY),
        (5, ApnsPriority.BASED_ON_POWER),
        (1, ApnsPriority.POWER_CONSIDERATIONS_OVER_ALL_OTHER_FACTORS),
    ],
)
def test_success(value, expect):
    priority = ApnsPriority(value)

    assert priority == expect


def test_value_error():
    with pytest.raises(ValueError) as e:
        _ = ApnsPriority(0)

    assert str(e.value) == "0 is not a valid ApnsPriority"
