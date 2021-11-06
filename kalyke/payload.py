from typing import Any, Dict, Optional, Union


class Alert(object):
    def __init__(
        self,
        title: Optional[str] = None,
        title_localized_key: Optional[str] = None,
        title_localized_args: Optional[str] = None,
        subtitle: Optional[str] = None,
        subtitle_loc_key: Optional[str] = None,
        subtitle_loc_args: Optional[str] = None,
        body: Optional[str] = None,
        body_localized_key: Optional[str] = None,
        body_localized_args: Optional[str] = None,
        action_localized_key: Optional[str] = None,
        action: Optional[str] = None,
        launch_image: Optional[str] = None,
    ) -> None:
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

    def dict(self) -> Dict[str, Any]:
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


class Sound(object):
    def __init__(self, critical: int = 1, name: str = "default", volume: int = 1) -> None:
        self.critical = critical
        self.name = name
        if 0 <= volume <= 1:
            self.volume = volume
        else:
            raise ValueError(
                "The volume for the critical alert’s sound.\n"
                "Set this to a value between 0 (silent) and 1 (full volume).\n"
                "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/"
                "generating_a_remote_notification#2990112"
            )

    def dict(self) -> Dict[str, Any]:
        return {
            "critical": self.critical,
            "name": self.name,
            "volume": self.volume,
        }


class Payload(object):
    def __init__(
        self,
        alert: Union[Optional[str], Optional[Alert]] = None,
        badge: Optional[int] = None,
        sound: Union[Optional[str], Optional[Sound]] = None,
        content_available: Optional[bool] = False,
        mutable_content: Optional[bool] = False,
        category: Optional[str] = None,
        thread_id: Optional[str] = None,
        target_content_id: Optional[str] = None,
        interruption_level: Optional[str] = None,
        relevance_score: Optional[float] = None,
        custom: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.content_available = content_available
        self.category = category
        self.mutable_content = mutable_content
        self.thread_id = thread_id
        self.target_content_id = target_content_id
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
        self.custom = custom

    def dict(self):
        result = {"aps": {}}
        if self.alert is not None:
            result["aps"]["alert"] = self.alert.dict() if isinstance(self.alert, Alert) else self.alert
        if self.badge is not None:
            result["aps"]["badge"] = self.badge
        if self.sound is not None:
            result["aps"]["sound"] = self.sound.dict() if isinstance(self.sound, Sound) else self.sound
        if self.content_available:
            result["aps"]["content-available"] = 1
        if self.mutable_content:
            result["aps"]["mutable-content"] = 1
        if self.thread_id is not None:
            result["aps"]["thread-id"] = self.thread_id
        if self.category is not None:
            result["aps"]["category"] = self.category
        if self.interruption_level is not None:
            result["aps"]["interruption-level"] = self.interruption_level
        if self.relevance_score is not None:
            result["aps"]["relevance-score"] = self.relevance_score
        if self.custom is not None:
            result.update(self.custom)

        return result
