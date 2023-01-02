import pytest

from kalyke import InterruptionLevel, Payload, PayloadAlert, exceptions


def test_dict_with_payload_alert():
    payload_alert = PayloadAlert(
        title="this is title",
        subtitle="this is subtitle",
        body="this is body",
    )
    payload = Payload(alert=payload_alert)
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps["alert"]["title"] == "this is title"
    assert aps["alert"]["subtitle"] == "this is subtitle"
    assert aps["alert"]["body"] == "this is body"


def test_dict_without_payload_alert():
    payload = Payload(
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
    )
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
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


def test_dict_relevance_score_out_of_range_exception():
    with pytest.raises(expected_exception=exceptions.RelevanceScoreOutOfRangeException) as e:
        _ = Payload(relevance_score=1.1)

    assert str(e.value) == "The system uses the relevance_score, a value between 0 and 1. Did set 1.1."


def test_dict_without_all():
    payload = Payload()
    data = payload.dict()

    assert "aps" in data
    aps = data["aps"]
    assert aps == {}
