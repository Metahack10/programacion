import reflex as rx
import App.estilos.styles as styles
from App.estilos.styles import Size as Size

def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            height = Size.BIG.value
        ),
        href = url,
        is_external = True,
    )

def link_cert(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            height = Size.VERY_BIG.value
        ),
        href = url,
        is_external = True,
    )