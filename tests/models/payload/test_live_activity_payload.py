from datetime import datetime

import pytest

from kalyke import InterruptionLevel, LiveActivityEvent, LiveActivityPayload, PayloadAlert, exceptions


@pytest.mark.parametrize(
    "attributes_type, attributes",
    [
        ("AdventureAttributes", None),
        (None, {"currentHealthLevel": 100, "eventDescription": "Adventure has begun!"}),
        (None, None),
    ],
    ids=["attributes_type is None", "attributes is None", "attributes_type and attributes are None"],
)
def test_live_activity_payload_event_is_start_value_error(attributes_type, attributes):
    with pytest.raises(ValueError) as e:
        _ = LiveActivityPayload(
            alert="this is alert",
            event=LiveActivityEvent.START,
        )

    assert (
        str(e.value)
        == "attributes_type and attributes must be specified when event is start.\nPlease see documentation: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification"  # noqa: E501
    )


def test_live_activity_payload_event_is_start_live_activity_attributes_is_not_json_serializable():
    with pytest.raises(exceptions.LiveActivityAttributesIsNotJSONSerializable) as e:
        _ = LiveActivityPayload(
            event=LiveActivityEvent.START,
            attributes_type="AdventureAttributes",
            attributes={"key": b"this is not JSON serializable."},
        )

    assert str(e.value) == "attributes is not JSON serializable."


def test_live_activity_payload_event_is_update_live_activity_content_state_is_not_json_serializable():
    with pytest.raises(exceptions.LiveActivityContentStateIsNotJSONSerializable) as e:
        _ = LiveActivityPayload(
            event=LiveActivityEvent.UPDATE,
            content_state={"key": b"this is not JSON serializable."},
        )

    assert str(e.value) == "content-state is not JSON serializable."


def test_dict_with_live_activity_payload_alert():
    payload_alert = PayloadAlert(
        title="this is title",
        subtitle="this is subtitle",
        body="this is body",
    )
    now = datetime.now()
    payload = LiveActivityPayload(
        alert=payload_alert,
        timestamp=now,
        event=LiveActivityEvent.UPDATE,
    )
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps["timestamp"] == int(now.timestamp())
    assert aps["event"] == "update"
    assert aps["content-state"] == {}
    assert aps["alert"]["title"] == "this is title"
    assert aps["alert"]["subtitle"] == "this is subtitle"
    assert aps["alert"]["body"] == "this is body"


def test_dict_without_live_activity_payload_alert():
    payload = LiveActivityPayload(
        alert="this is alert",
        badge=22,
        sound="custom_sound",
        thread_id="stub_thread_id",
        category="stub_category",
        content_available=True,
        mutable_content=True,
        target_content_identifier="stub_target_content_identifier",
        interruption_level=InterruptionLevel.PASSIVE,
        relevance_score=0.4,
        filter_criteria="stub_filter_criteria",
        custom={"stub_key": "stub_value"},
        event=LiveActivityEvent.UPDATE,
    )
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps["event"] == "update"
    assert aps["alert"] == "this is alert"
    assert aps["badge"] == 22
    assert aps["sound"] == "custom_sound"
    assert aps["thread-id"] == "stub_thread_id"
    assert aps["category"] == "stub_category"
    assert aps["content-available"] == 1
    assert aps["mutable-content"] == 1
    assert aps["target-content-identifier"] == "stub_target_content_identifier"
    assert aps["interruption-level"] == "passive"
    assert aps["relevance-score"] == 0.4
    assert aps["filter-criteria"] == "stub_filter_criteria"
    assert data["stub_key"] == "stub_value"


def test_dict_not_relevance_score_out_of_range_exception():
    payload = LiveActivityPayload(
        relevance_score=100,
        event=LiveActivityEvent.UPDATE,
    )
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps["relevance-score"] == 100


def test_dict_without_all():
    now = datetime.now()
    payload = LiveActivityPayload(timestamp=now, event=LiveActivityEvent.UPDATE)
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps == {
        "event": "update",
        "timestamp": int(now.timestamp()),
        "content-state": {},
    }
