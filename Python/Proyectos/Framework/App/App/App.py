import reflex as rx
from App.componentes.navbar import navbar
from App.vistas.cabecera.cabecera import cabecera
from App.vistas.enlaces.enlaces import enlaces
from App.componentes.pie import pie
from App.estilos.styles import Size as Size
import App.estilos.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                cabecera(),
                enlaces(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding = Size.BIG.value
            )
        ),
        pie()
    )


app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title = "Metahack | Especialista en Ciberseguridad",
    description = "Hola, mi nombre es Jorge Lopez alias Metahack. Soy Ingeniero Informático especialista en Ciberseguridad y hacking ético.",
    image = "./Left Arrown.ico"
)
#app.compile()