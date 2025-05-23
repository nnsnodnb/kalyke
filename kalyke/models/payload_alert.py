from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass(frozen=True)
class PayloadAlert:
    title: Optional[str] = field(default=None)
    subtitle: Optional[str] = field(default=None)
    body: Optional[str] = field(default=None)
    launch_image: Optional[str] = field(default=None)
    title_loc_key: Optional[str] = field(default=None)
    title_loc_args: Optional[list[str]] = field(default=None)
    subtitle_loc_key: Optional[str] = field(default=None)
    subtitle_loc_args: Optional[list[str]] = field(default=None)
    loc_key: Optional[str] = field(default=None)
    loc_args: Optional[list[str]] = field(default=None)

    def dict(self) -> dict[str, Union[str, list[str]]]:
        alert: dict[str, Optional[Union[str, list[str]]]] = {
            "title": self.title,
            "subtitle": self.subtitle,
            "body": self.body,
            "launch-image": self.launch_image,
            "title-loc-key": self.title_loc_key,
            "title-loc-args": self.title_loc_args,
            "subtitle-loc-key": self.subtitle_loc_key,
            "subtitle-loc-args": self.subtitle_loc_args,
            "loc-key": self.loc_key,
            "loc-args": self.loc_args,
        }
        attached_alert: dict[str, Union[str, list[str]]] = {k: v for k, v in alert.items() if v is not None}
        return attached_alert
