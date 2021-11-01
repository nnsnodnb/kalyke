class PayloadAlert(object):
    def __init__(
        self,
        title=None,
        title_localized_key=None,
        title_localized_args=None,
        subtitle=None,
        subtitle_loc_key=None,
        subtitle_loc_args=None,
        body=None,
        body_localized_key=None,
        body_localized_args=None,
        action_localized_key=None,
        action=None,
        launch_image=None,
    ):
        self.title = title
        self.title_localized_key = title_localized_key
        self.title_localized_args = title_localized_args
        self.subtitle = subtitle
        self.subtitle_loc_key = subtitle_loc_key
        self.subtitle_loc_args = subtitle_loc_args
        self.body = body
        self.body_localized_key = body_localized_key
        self.body_localized_args = body_localized_args
        self.action_localized_key = action_localized_key
        self.action = action
        self.launch_image = launch_image

    def dict(self):
        result = {}

        if self.title:
            result["title"] = self.title
        if self.title_localized_key:
            result["title-loc-key"] = self.title_localized_key
        if self.title_localized_args:
            result["title-loc-args"] = self.title_localized_args

        if self.subtitle:
            result["subtitle"] = self.subtitle
        if self.subtitle_loc_key:
            result["subtitle-loc-key"] = self.subtitle_loc_key
        if self.subtitle_loc_args:
            result["subtitle-loc-args"] = self.subtitle_loc_args

        if self.body:
            result["body"] = self.body
        if self.body_localized_key:
            result["loc-key"] = self.body_localized_key
        if self.body_localized_args:
            result["loc-args"] = self.body_localized_args

        if self.action_localized_key:
            result["action-loc-key"] = self.action_localized_key
        if self.action:
            result["action"] = self.action

        if self.launch_image:
            result["launch-image"] = self.launch_image

        return result


class Payload(object):
    def __init__(
        self,
        alert=None,
        badge=None,
        sound=None,
        content_available=False,
        mutable_content=False,
        category=None,
        url_args=None,
        custom=None,
        thread_id=None,
        interruption_level=None,
        relevance_score=None,
    ):
        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.content_available = content_available
        self.category = category
        self.url_args = url_args
        self.custom = custom
        self.mutable_content = mutable_content
        self.thread_id = thread_id
        if interruption_level is not None and interruption_level not in [
            "passive",
            "active",
            "time-sensitive",
            "critical",
        ]:
            raise ValueError(
                "Invalid value for interruption_level.\n"
                "Please choice from passive, active, time-sensitive or critical.\n"
                "https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel"
            )
        self.interruption_level = interruption_level
        if relevance_score is None:
            self.relevance_score = None
        elif (isinstance(relevance_score, int) or isinstance(relevance_score, float)) and 0 <= relevance_score <= 1:
            self.relevance_score = relevance_score
        else:
            raise ValueError(
                "Invalid value for relevance_score.\n"
                "a value between 0\n"
                "https://developer.apple.com/documentation/usernotifications/unnotificationcontent/"
                "3821031-relevancescore"
            )

    def dict(self):
        result = {"aps": {}}
        if self.alert is not None:
            if isinstance(self.alert, PayloadAlert):
                result["aps"]["alert"] = self.alert.dict()
            else:
                result["aps"]["alert"] = self.alert
        if self.badge is not None:
            result["aps"]["badge"] = self.badge
        if self.sound is not None:
            result["aps"]["sound"] = self.sound
        if self.content_available:
            result["aps"]["content-available"] = 1
        if self.mutable_content:
            result["aps"]["mutable-content"] = 1
        if self.thread_id is not None:
            result["aps"]["thread-id"] = self.thread_id
        if self.category is not None:
            result["aps"]["category"] = self.category
        if self.url_args is not None:
            result["aps"]["url-args"] = self.url_args
        if self.interruption_level is not None:
            result["aps"]["interruption-level"] = self.interruption_level
        if self.relevance_score is not None:
            result["aps"]["relevance-score"] = self.relevance_score
        if self.custom is not None:
            result.update(self.custom)

        return result
