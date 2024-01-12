import uuid

import pytest

from kalyke.models import ApnsPriority, ApnsPushType, VoIPApnsConfig


def test_make_headers():
    identifier = uuid.uuid4()
    config = VoIPApnsConfig(
        topic="com.example.App.voip",
        identifier=str(identifier),
        expiration=0,
        priority=ApnsPriority.BASED_ON_POWER,
        collapse_id="stub_collapse_id",
    )
    data = config.make_headers()

    assert data["apns-push-type"] == "voip"
    assert data["apns-id"] == str(identifier)
    assert data["apns-expiration"] == "0"
    assert data["apns-priority"] == "5"
    assert data["apns-topic"] == "com.example.App.voip"
    assert data["apns-collapse-id"] == "stub_collapse_id"
    assert "user-agent" in data


def test_value_error_topic():
    with pytest.raises(ValueError) as e:
        _ = VoIPApnsConfig(topic="com.example.App")

    assert str(e.value) == "topic must end with .voip, but com.example.App."


def test_value_error_identifier():
    with pytest.raises(ValueError) as e:
        _ = VoIPApnsConfig(topic="com.example.App.voip", identifier="invalid-uuid4-format-identifier")

    assert str(e.value) == "invalid-uuid4-format-identifier is invalid format."


def test_make_headers_ignore_available_params():
    config = VoIPApnsConfig(
        topic="com.example.App.voip",
    )
    data = config.make_headers()

    assert data["apns-push-type"] == "voip"
    assert "apns-id" not in data
    assert "apns-expiration" in data
    assert data["apns-priority"] == "10"
    assert data["apns-topic"] == "com.example.App.voip"
    assert "apns-collapse-id" not in data
    assert "user-agent" in data
