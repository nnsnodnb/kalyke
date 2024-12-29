from enum import Enum


class ApnsPushType(Enum):
    ALERT = "alert"
    BACKGROUND = "background"
    LOCATION = "location"
    VOIP = "voip"
    COMPLICATION = "complication"
    FILE_PROVIDER = "fileprovider"
    MDM = "mdm"
    LIVEACTIVITY = "liveactivity"
