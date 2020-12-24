from kalyke.payload import Payload, PayloadAlert


def test_payload_dict() -> None:
    payload = Payload(alert="this is alert", badge=1, sound="default")
    result = payload.dict()

    assert result["aps"]["alert"] == "this is alert"
    assert result["aps"]["badge"] == 1
    assert result["aps"]["sound"] == "default"


def test_payload_with_payload_alert() -> None:
    alert = PayloadAlert(title="this is title", body="this is body")
    custom = {"custom_key": "custom value"}
    payload = Payload(
        alert=alert,
        badge=1,
        sound="default",
        content_available=True,
        mutable_content=True,
        thread_id="this_is_thread_identifier",
        category="notification_category",
        url_args="url_arguments",
        custom=custom,
    )
    result = payload.dict()

    assert result["aps"]["alert"]["title"] == "this is title"
    assert result["aps"]["alert"]["body"] == "this is body"
    assert result["aps"]["badge"] == 1
    assert result["aps"]["sound"] == "default"
    assert result["aps"]["content-available"] == 1
    assert result["aps"]["mutable-content"] == 1
    assert result["aps"]["thread-id"] == "this_is_thread_identifier"
    assert result["aps"]["category"] == "notification_category"
    assert result["aps"]["url-args"] == "url_arguments"
    assert result["custom_key"] == "custom value"
