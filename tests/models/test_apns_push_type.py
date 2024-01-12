import pytest

from kalyke import ApnsPushType


@pytest.mark.parametrize(
    "value, expect",
    [
        ("alert", ApnsPushType.ALERT),
        ("background", ApnsPushType.BACKGROUND),
        ("location", ApnsPushType.LOCATION),
        ("voip", ApnsPushType.VOIP),
        ("complication", ApnsPushType.COMPLICATION),
        ("fileprovider", ApnsPushType.FILE_PROVIDER),
        ("mdm", ApnsPushType.MDM),
        ("liveactivity", ApnsPushType.LIVEACTIVITY),
    ],
    ids=["alert", "background", "location", "voip", "complication", "fileprovider", "mdm", "liveactivity"],
)
def test_success(value, expect):
    apns_push_type = ApnsPushType(value)

    assert apns_push_type == expect


def test_value_error():
    with pytest.raises(ValueError) as e:
        _ = ApnsPushType("stub")

    assert str(e.value) == "'stub' is not a valid ApnsPushType"
