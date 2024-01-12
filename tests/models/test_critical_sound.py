import pytest

from kalyke import CriticalSound, exceptions


def test_dict():
    cs = CriticalSound(critical=True, volume=1, name="stub_name")
    data = cs.dict()

    assert data["critical"] == 1
    assert data["volume"] == 1
    assert data["name"] == "stub_name"


@pytest.mark.parametrize(
    "volume",
    [-0.01, 1.01],
    ids=["negative", "greater than 1.0"],
)
def test_volume_out_of_range_exception(volume):
    with pytest.raises(exceptions.VolumeOutOfRangeException) as e:
        _ = CriticalSound(critical=True, volume=volume)

    assert str(e.value) == f"The volume must be a value between 0.0 and 1.0. Did set {volume}."
