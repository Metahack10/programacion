import reflex as rx
from App.componentes.link_icon import link_icon
from App.estilos.styles import Size as Size

def cabecera() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
            src="./perfil.png", 
            fallback="JL", 
            size="8", 
            radius="full"
            ),
            rx.vstack(
                rx.hstack(
                    rx.heading("JORGE LOPEZ", 
                            size = "9",
                            weight = "medium"
                    ),
                    rx.heading("(Metahack)", 
                            size = "7",
                            weight = "light",
                            margin_top = "20px"
                    ),
                    padding_top = "5px"
                ),
                rx.heading("CYBERSECURITY SPECIALIST", 
                        size = "8",
                        weight = "regular",
                        padding_top = "10px"
                ),
                rx.flex(
                    link_icon("https://www.linkedin.com/in/jorge-lopez-vicente/", "Linkedin"),
                    rx.spacer(),
                    link_icon("https://github.com/Metahack10", "Github"),
                    rx.spacer(),
                    link_icon("https://www.youtube.com/@JorgeLopez-br4mt", "Youtube"),
                    width = "80%",
                    align = "center"
                )
            ),
            align = "center",
            align_items = "start"
        ),
        rx.text("""Soy ingeniero Informático especialista en Ciberseguridad, 
                cuento con más de 10 años de experiencia especializada en auditoría de sistemas 
                y seguridad de la información, con un enfoque particular en el sector bancario y financiero."""),
        align_items = "start",
        spacing = Size.BIG.value
    )