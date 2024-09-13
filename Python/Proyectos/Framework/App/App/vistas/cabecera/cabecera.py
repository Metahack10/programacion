import reflex as rx

def cabecera() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            src="./perfil.png", 
            fallback="JL", 
            size="8", 
            radius="full"
        ),
        rx.text("@Metahack",),
        rx.text("HOLA👋 MI NOMBRE ES JORGE LOPEZ(Metahack)"),
        rx.text("""Soy ingeniero Informático especialista en Ciberseguridad, 
                cuento con más de 10 años de experiencia especializada en auditoría de sistemas 
                y seguridad de la información, con un enfoque particular en el sector bancario y financiero.""")
    )