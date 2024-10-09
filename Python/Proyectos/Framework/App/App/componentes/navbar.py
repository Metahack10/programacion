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
        rx.flex(
            rx.link(rx.text("Sobre mí", class_name = "nav_boton"), href = "#Sobre_mi"),
            rx.link(rx.text("Experiencia", class_name = "nav_boton"), href = "#Experiencia"),
            rx.link(rx.text("Certificaciones", class_name = "nav_boton"), href = "#Certificaciones"),
            rx.link(rx.text("Habilidades", class_name = "nav_boton"), href = "#habilidades"),
            rx.link(rx.text("Aportes", class_name = "nav_boton"), href = "#Aportes"),
            rx.link(
                rx.hstack(
                    rx.image(
                        src = "resume.png",
                        height = Size.LARGE.value,
                        margin_left = "15px"
                    ),
                    rx.text("Mi Curriculum", class_name = "nav_boton", margin_left = "-3px")
                ),
                is_external = True,
                href = "Cv/resume.pdf"
            ),
            class_name="nav_menu"
        ),
        position="sticky",
        bg = Color.Nav.value,
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index="999",
        top = "0",
        style=dict(
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.5)"
        )
    )