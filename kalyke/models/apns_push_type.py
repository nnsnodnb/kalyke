from enum import Enum


class ApnsPushType(Enum):
    ALERT: str = "alert"
    BACKGROUND: str = "background"
    LOCATION: str = "location"
    VOIP: str = "voip"
    COMPLICATION: str = "complication"
    FILE_PROVIDER: str = "fileprovider"
    MDM: str = "mdm"
    LIVEACTIVITY: str = "liveactivity"
