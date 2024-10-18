import reflex as rx
import App.estilos.styles as styles
from App.estilos.styles import Size as Size
from App.estilos.colors import Color as Color

def link_icon(url: str, image: str, titulo: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            title = titulo,
            height = rx.breakpoints(initial = Size.MEDIUM.value, sm = Size.LARGE.value, lg = Size.BIG.value),
            width = "auto"
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
                size = rx.breakpoints(initial = "1", sm = "1", lg = "2"),
                color = Color.TITULO.value,
                align = "center",
                #padding = "5px",
                margin = "5px"
        ),
        rx.image(
            src = image,
            title = descripcion,
            class_name = clase,
            height = rx.breakpoints(initial = "40px", sm = "60px", lg = "80px"),
            width = rx.breakpoints(initial = "40px", sm = "60px", lg = "80px"),
            background_color = "transparent",
            border = "none",
            clip_path = "inset(1%)"
        ),
        class_name = "certificaciones",
        href = url,
        is_external = True,
        padding_bottom = "10px",
        padding_top = "10px",
        padding_left = "5px",
        padding_right = "5px"
    )