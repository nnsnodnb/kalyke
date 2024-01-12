import uuid

import pytest

from kalyke.models import ApnsConfig, ApnsPushType, ApnsPriority


def test_make_headers():
    identifier = uuid.uuid4()
    config = ApnsConfig(
        topic="com.example.App",
        push_type=ApnsPushType.ALERT,
        identifier=str(identifier),
        expiration=0,
        priority=ApnsPriority.BASED_ON_POWER,
        collapse_id="stub_collapse_id",
    )
    data = config.make_headers()

    assert data["apns-push-type"] == "alert"
    assert data["apns-id"] == str(identifier)
    assert data["apns-expiration"] == "0"
    assert data["apns-priority"] == "5"
    assert data["apns-topic"] == "com.example.App"
    assert data["apns-collapse-id"] == "stub_collapse_id"
    assert "user-agent" in data


def test_value_error():
    with pytest.raises(ValueError) as e:
        _ = ApnsConfig(topic="com.example.App", identifier="invalid-uuid4-format-identifier")

    assert str(e.value) == "invalid-uuid4-format-identifier is invalid format."


def test_make_headers_ignore_available_params():
    config = ApnsConfig(
        topic="com.example.App",
    )
    data = config.make_headers()

    assert data["apns-push-type"] == "alert"
    assert "apns-id" not in data
    assert "apns-expiration" in data
    assert data["apns-priority"] == "10"
    assert data["apns-topic"] == "com.example.App"
    assert "apns-collapse-id" not in data
    assert "user-agent" in data
