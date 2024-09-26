import reflex as rx
import App.estilos.styles as styles
from App.estilos.styles import Size as Size
from App.estilos.colors import TextColor as TextColor

def expe(logo: str, empresa: str, cargo: str, roles: str) -> rx.Component:
    return rx.hstack(
        rx.image(
            src = logo,
            border_radius = "50%",
            object_fit = "cover",
            width = "40px",
            height = "40px"
        ),
        rx.vstack(
            rx.text(empresa, style=styles.text_title_style, margin_top = "-5px",
            color = TextColor.HEADER.value,
            size = "5"
            ),
            rx.text(cargo, style=styles.text_subtitle_style, margin_top = "-8px",
            color = TextColor.BODY.value,
            size = "5",
            padding = "0px"
            ),
            rx.text(roles, style=styles.text_body_style, margin_top = "-3px",
            color = TextColor.FOOTER.value
            ),
        )
    )