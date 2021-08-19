from typing import Any, Dict, Optional, Union


class PayloadAlert(object):
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

    def dict(self) -> Dict[str, str]:
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
        alert: Union[Optional[str], PayloadAlert] = None,
        badge: Optional[int] = None,
        sound: Optional[str] = None,
        content_available: bool = False,
        mutable_content: bool = False,
        category: Optional[str] = None,
        url_args: Optional[str] = None,
        custom: Optional[Dict[str, str]] = None,
        thread_id: Optional[str] = None,
    ) -> None:
        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.content_available = content_available
        self.category = category
        self.url_args = url_args
        self.custom = custom
        self.mutable_content = mutable_content
        self.thread_id = thread_id

    def dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {"aps": {}}

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
        if self.custom is not None:
            result.update(self.custom)

        return result
