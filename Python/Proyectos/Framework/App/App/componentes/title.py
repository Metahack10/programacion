import reflex as rx
import App.estilos.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        font_size = "6",
        style = styles.title_style
    )