from dataclasses import dataclass, field


@dataclass(frozen=True)
class PayloadAlert:
    title: str | None = field(default=None)
    subtitle: str | None = field(default=None)
    body: str | None = field(default=None)
    launch_image: str | None = field(default=None)
    title_loc_key: str | None = field(default=None)
    title_loc_args: list[str] | None = field(default=None)
    subtitle_loc_key: str | None = field(default=None)
    subtitle_loc_args: list[str] | None = field(default=None)
    loc_key: str | None = field(default=None)
    loc_args: list[str] | None = field(default=None)

    def dict(self) -> dict[str, str | list[str]]:
        alert: dict[str, str | list[str] | None] = {
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
        attached_alert: dict[str, str | list[str]] = {k: v for k, v in alert.items() if v is not None}
        return attached_alert
