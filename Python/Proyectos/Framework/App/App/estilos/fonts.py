from enum import Enum

class Font(Enum):
    DEFAULT = "Poppins"
    TITLE = "Prompt"
    LOGO = "Fira Code"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"
    BIG = "700"