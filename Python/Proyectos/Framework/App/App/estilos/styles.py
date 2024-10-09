import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FWeight

#? Constantes
MAX_WIDTH = "800px"
bg_svg = "bg_constelacion2.svg"

#* Sizes
class Size(Enum):
    SMALL = "0.5em"
    SMEDIUM = "0.6em"
    MEDIUM = "0.8em"
    SDEFAULT = "0.9em"
    DEFAULT = "1em"
    SLARGE = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    XX_BIG = "5em"
    EXTRA_BIG = "6em"

#! Styles
BASE_STYLE = {
    "background_color": "#330033",
    "background_image": f"url({bg_svg})",
    "font_family": Font.DEFAULT.value,
    "font_weight": FWeight.LIGHT,
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
    font_family = Font.TITLE.value,
    font_weight = FWeight.MEDIUM
)

button_body_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.BODY.value,
    font_family = Font.DEFAULT.value,
    font_weight = FWeight.LIGHT
)

text_title_style = dict(
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value,
    font_weight = FWeight.BIG
)

text_subtitle_style = dict(
    color = TextColor.BODY.value,
    font_family = Font.TITLE.value,
    font_weight = FWeight.LIGHT
)

text_body_style = dict(
    color = TextColor.BODY.value,
    font_family = Font.DEFAULT.value,
    font_weight = FWeight.LIGHT
)



title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value,
    font_weight = FWeight.BIG
)

navbar_title_style = dict(
    font_family = Font.LOGO.value,
    font_size = Size.LARGE.value,
    font_weight = FWeight.BIG
)


