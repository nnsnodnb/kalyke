from kalyke.payload import PayloadAlert


def test_payload_alert_dict() -> None:
    alert = PayloadAlert(
        title="this is title",
        title_localized_key="title_key",
        title_localized_args="title_args",
        subtitle="this is subtitle",
        subtitle_loc_key="subtitle_key",
        subtitle_loc_args="subtitle_args",
        body="this is body",
        body_localized_key="body_key",
        body_localized_args="body_args",
        action_localized_key="action_key",
        action="this is action",
        launch_image="launch_image.png",
    )
    result = alert.dict()

    assert result["title"] == "this is title"
    assert result["title-loc-key"] == "title_key"
    assert result["title-loc-args"] == "title_args"
    assert result["subtitle"] == "this is subtitle"
    assert result["subtitle-loc-key"] == "subtitle_key"
    assert result["subtitle-loc-args"] == "subtitle_args"
    assert result["body"] == "this is body"
    assert result["loc-key"] == "body_key"
    assert result["loc-args"] == "body_args"
    assert result["action-loc-key"] == "action_key"
    assert result["action"] == "this is action"
    assert result["launch-image"] == "launch_image.png"
