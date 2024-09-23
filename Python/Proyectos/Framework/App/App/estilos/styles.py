import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#? Constantes
MAX_WIDTH = "740px"
bg_svg = "bg_constelacion2.svg"

#* Sizes
class Size(Enum):
    SMALL = "0.5em"
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
    #"background_color": Color.BACKGROUND.value,
    "background_color": "#330033",
    "background_image": f"url({bg_svg})",
    #"background_size": "cover",
    #"background-position": "center",
    #"opacity": "0.6",
    #"background-repeat": "no-repeat",
    #"height": "100vh",
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

text_title_style = dict(
    font_size = Size.SLARGE.value,
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value
)

text_subtitle_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
    font_family = Font.DEFAULT.value
)

text_body_style = dict(
    font_size = Size.SDEFAULT.value,
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


