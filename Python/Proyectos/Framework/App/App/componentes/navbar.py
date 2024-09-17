import reflex as rx
from App.estilos.styles import Size as Size
from App.estilos.colors import Color as Color
import App.estilos.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.strong("©Meta", as_= "span", color = Color.PRIMARY.value),
            rx.text.strong("hack", as_ = "span", color = Color.SECONDARY.value),
            style = styles.navbar_title_style
        ),
        position="sticky",
        bg = Color.Nav.value,
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index="999",
        top = "0"
    )