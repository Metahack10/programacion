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
                size="9", 
                radius="full",
                color = TextColor.BODY.value,
                bg = Color.BORDE.value,
                padding = "3px",
                border = "6px",
                margin_top = "10px"
            ),
            rx.vstack(
                rx.hstack(
                    rx.heading("JORGE LOPEZ", 
                            size = "9",
                            weight = "medium",
                            color = Color.TITULO.value,
                            style = styles.title_style,
                            margin_top = "10px",
                            padding = "5px",
                            white_space = "nowrap"
                    ),
                    rx.heading("(Metahack)", 
                            size = "7",
                            weight = "light",
                            margin_top = "10px",
                            color = Color.ALIAS.value,
                            class_name = "neon-text",
                            style = styles.title_style
                    ),
                    padding_top = "5px"
                ),
                rx.heading("CYBERSECURITY SPECIALIST", 
                        size = "8",
                        weight = "regular",
                        padding_left = "5px",
                        padding_top = "5px",
                        padding_button = "3px",
                        color = Color.ROL.value,
                        style = styles.title_style,
                        margin_top = "0px"
                ),
                rx.flex(
                    link_icon("https://www.linkedin.com/in/jorge-lopez-vicente/", "Rsociales/linkedin.png", "LinkedIn"),
                    rx.spacer(),
                    link_icon("https://github.com/Metahack10", "Rsociales/Github.png", "GitHub"),
                    rx.spacer(),
                    link_icon("https://www.youtube.com/@JorgeLopez-br4mt", "Rsociales/youtube.png", "YouTube"),
                    rx.spacer(),
                    link_icon("mailto:pkflopez@gmail.com", "Rsociales/email.png", "pkflopez@gmail.com"),
                    width = "70%",
                    padding_left = "5px"
                )
            ),
            align = "center",
            align_items = "start"
        ),
        align_items = "start",
        spacing = "6"
    )