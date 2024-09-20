import reflex as rx
from App.componentes.title import title as title
from App.estilos.colors import TextColor as TextColor

def aboutme() -> rx.Component:
    return rx.vstack(
        title("👨‍💻Sobre mí"),
        rx.text("""Soy ingeniero Informático especialista en Ciberseguridad, 
                cuento con más de 10 años de experiencia especializada en auditoría de sistemas 
                y seguridad de la información, con un enfoque particular en el sector bancario y financiero.""",
                color = TextColor.BODY.value,
                size = "5"
        ),
        align_items = "start",
        spacing = "4"
    )