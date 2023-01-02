from kalyke.models import PayloadAlert


def test_dict_with_all():
    payload_alert = PayloadAlert(
        title="this is title",
        subtitle="this is subtitle",
        body="this is body",
        launch_image="stub_launch_image",
        title_loc_key="this_is_title_loc_key",
        title_loc_args=["this_is_title_loc_args"],
        subtitle_loc_key="this_is_subtitle_loc_key",
        subtitle_loc_args=["this_is_subtitle_loc_args"],
        loc_key="this_is_loc_key",
        loc_args=["this_is_loc_args"],
    )
    data = payload_alert.dict()

    assert data["title"] == "this is title"
    assert data["subtitle"] == "this is subtitle"
    assert data["body"] == "this is body"
    assert data["launch-image"] == "stub_launch_image"
    assert data["title-loc-key"] == "this_is_title_loc_key"
    assert data["title-loc-args"] == ["this_is_title_loc_args"]
    assert data["subtitle-loc-key"] == "this_is_subtitle_loc_key"
    assert data["subtitle-loc-args"] == ["this_is_subtitle_loc_args"]
    assert data["loc-key"] == "this_is_loc_key"
    assert data["loc-args"] == ["this_is_loc_args"]


def test_dict_without_all():
    payload_alert = PayloadAlert()
    data = payload_alert.dict()

    assert data == {}
