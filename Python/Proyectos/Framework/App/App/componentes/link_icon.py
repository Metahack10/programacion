import reflex as rx
import App.estilos.styles as styles
from App.estilos.styles import Size as Size
from App.estilos.colors import Color as Color

def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            height = Size.BIG.value
        ),
        href = url,
        is_external = True,
    )

def link_cert(titulo: str, url: str, image: str, descripcion: str) -> rx.Component:
    if image == "Certi/ISO27032.png":
        clase = "img2"
    else:
        clase = "img"
    return rx.link(
        rx.heading(
                titulo,
                size = "2",
                color = Color.TITULO.value,
                align = "center"
        ),
        rx.image(
            src = image,
            title = descripcion,
            padding = "5px",
            class_name = clase
        ),
        class_name = "certificaciones",
        href = url,
        is_external = True
    )