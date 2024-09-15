import reflex as rx
import App.estilos.styles as styles

def link_icon(url: str, icono: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag = icono
        ),
        href = url,
        is_external = True
    )