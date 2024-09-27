import reflex as rx
from App.estilos.colors import Color as Color

def skill_icon(image: str, titulo: str) -> rx.Component:
        return rx.image(
                src = image,
                title = titulo,
                class_name = "caru_img"
        )
