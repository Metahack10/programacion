import reflex as rx
import App.estilos.styles as styles

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="calendar"
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(text, style=styles.button_body_style)
                )
            )
        ),
        href=url,
        is_external = True,
        width="100%"
    )