import reflex as rx
import App.estilos.styles as styles
from App.estilos.styles import Size as Size

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="Twitch",
                    width = styles.Size.BIG.value,
                    height = styles.Size.BIG.value,
                    margin = Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style, margin_top = "5px"),
                    rx.text(body, style=styles.button_body_style, margin_top = "-5px"),
                    align_items = "start",
                    spacing = Size.SMALL.value
                )
            )
        ),
        href=url,
        is_external = True,
        width="100%"
    )