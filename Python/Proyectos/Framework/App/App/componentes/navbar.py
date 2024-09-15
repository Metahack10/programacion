import reflex as rx
from App.estilos.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Metahack"
                ),
                position="sticky",
                bg = "blue",
                padding_x = Size.DEFAULT.value,
                padding_y = Size.SMALL.value,
                z_index="999",
                top = "0"
    )