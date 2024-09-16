import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

#? Constantes
MAX_WIDTH = "700px"

#* Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

#! Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "Color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

button_title_style = dict(
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)