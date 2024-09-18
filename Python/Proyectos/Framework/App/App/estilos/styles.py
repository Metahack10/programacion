import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#? Constantes
MAX_WIDTH = "740px"

#* Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    SLARGE = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

#! Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "Color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        },
        "cursor": "pointer"
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

button_title_style = dict(
    font_size = Size.SLARGE.value,
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value
)

button_body_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.BODY.value,
    font_family = Font.DEFAULT.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value
)

navbar_title_style = dict(
    font_family = Font.LOGO.value,
    font_size = Size.LARGE.value
)