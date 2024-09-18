import reflex as rx
from App.componentes.link_icon import link_icon
from App.estilos.styles import Size as Size
from App.estilos.colors import TextColor as TextColor
from App.estilos.colors import Color as Color
import App.estilos.styles as styles

def cabecera() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="./perfil.png", 
                fallback="JL", 
                size="8", 
                radius="full",
                color = TextColor.BODY.value,
                bg = Color.BORDE.value,
                padding = "3px",
                border = "6px"
            ),
            rx.vstack(
                rx.hstack(
                    rx.heading("JORGE LOPEZ", 
                            size = "9",
                            weight = "medium",
                            color = Color.TITULO.value
                    ),
                    rx.heading("(Metahack)", 
                            size = "7",
                            weight = "light",
                            margin_top = "20px",
                            color = Color.ALIAS.value,
                            style = styles.alias_style
                    ),
                    padding_top = "5px"
                ),
                rx.heading("CYBERSECURITY SPECIALIST", 
                        size = "8",
                        weight = "regular",
                        padding_top = "10px",
                        color = Color.ROL.value
                ),
                rx.flex(
                    link_icon("https://www.linkedin.com/in/jorge-lopez-vicente/", "linkedin.png"),
                    rx.spacer(),
                    link_icon("https://github.com/Metahack10", "Github3(1).png"),
                    rx.spacer(),
                    link_icon("https://www.youtube.com/@JorgeLopez-br4mt", "youtube.png"),
                    rx.spacer(),
                    link_icon("mail to:pkflopez@gmail.com", "email.png"),
                    width = "70%"
                )
            ),
            align = "center",
            align_items = "start"
        ),
        align_items = "start",
        spacing = "6"
    )