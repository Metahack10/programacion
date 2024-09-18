import reflex as rx
import datetime
from App.estilos.styles import Size as Size
import App.estilos.styles as styles
from App.estilos.colors import TextColor as TextColor

def pie() -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.image(
                    src="favicon.ico",
                    height = Size.VERY_BIG
                ),
                rx.link("© Metahack",
                        href="https://github.com/Metahack10",
                        is_external=True,
                        font_size = Size.MEDIUM.value
                    ),
                rx.text(
                        f"protegiendo el activo más importante para las empresas, desde 2013 - {datetime.date.today().year}", 
                        font_size = Size.MEDIUM.value,
                        margin_top = "-10px"
                    ),
                margin_bottom = Size.BIG.value,
                align = "center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                color = TextColor.FOOTER.value
            )
        )