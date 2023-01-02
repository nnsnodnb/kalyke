from typing import Dict, List, Optional, Union


class PayloadAlert:
    title: Optional[str]
    subtitle: Optional[str]
    body: Optional[str]
    launch_image: Optional[str]
    title_loc_key: Optional[str]
    title_loc_args: Optional[List[str]]
    subtitle_loc_key: Optional[str]
    subtitle_loc_args: Optional[List[str]]
    loc_key: Optional[str]
    loc_args: Optional[List[str]]

    def __init__(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        body: Optional[str] = None,
        launch_image: Optional[str] = None,
        title_loc_key: Optional[str] = None,
        title_loc_args: Optional[List[str]] = None,
        subtitle_loc_key: Optional[str] = None,
        subtitle_loc_args: Optional[List[str]] = None,
        loc_key: Optional[str] = None,
        loc_args: Optional[List[str]] = None,
    ) -> None:
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.launch_image = launch_image
        self.title_loc_key = title_loc_key
        self.title_loc_args = title_loc_args
        self.subtitle_loc_key = subtitle_loc_key
        self.subtitle_loc_args = subtitle_loc_args
        self.loc_key = loc_key
        self.loc_args = loc_args

    def dict(self) -> Dict[str, Union[str, List[str]]]:
        alert: Dict[str, Union[str, List[str]]] = {}
        if self.title:
            alert["title"] = self.title
        if self.subtitle:
            alert["subtitle"] = self.subtitle
        if self.body:
            alert["body"] = self.body
        if self.launch_image:
            alert["launch-image"] = self.launch_image
        if self.title_loc_key:
            alert["title-loc-key"] = self.title_loc_key
        if self.title_loc_args:
            alert["title-loc-args"] = self.title_loc_args
        if self.subtitle_loc_key:
            alert["subtitle-loc-key"] = self.subtitle_loc_key
        if self.subtitle_loc_args:
            alert["subtitle-loc-args"] = self.subtitle_loc_args
        if self.loc_key:
            alert["loc-key"] = self.loc_key
        if self.loc_args:
            alert["loc-args"] = self.loc_args

        return alert
