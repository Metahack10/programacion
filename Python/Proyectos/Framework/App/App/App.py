import reflex as rx
from App.componentes.navbar import navbar
from App.vistas.cabecera.cabecera import cabecera
from App.vistas.enlaces.certificaciones import certificaciones
from App.vistas.About.aboutme import aboutme
from App.vistas.Experiencia.experiencia import experiencia
from App.vistas.habilidades.skills import habilidades
from App.vistas.Aportes.aportes import aportes
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
                aboutme(),
                experiencia(),
                certificaciones(),
                aportes(),
                habilidades(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding = Size.BIG.value,
                bg = "rgba(8, 20, 45, 0.8)",
                border_radius = "15px",
                box_shadow = "0px 4px 15px 20px rgba(36, 41, 68, 0.3)"
            )
        ),
        pie()
    )

app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        "/styles.css"
    ]
)

app.add_page(
    index,
    title = "Metahack | Especialista en Ciberseguridad",
    description = "Hola, mi nombre es Jorge Lopez alias Metahack. Soy Ingeniero Informático especialista en Ciberseguridad y hacking ético.",
)
#app.compile()