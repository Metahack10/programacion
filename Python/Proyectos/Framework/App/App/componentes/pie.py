import reflex as rx
import datetime

def pie() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link("© Metahack",
                href="https://github.com/Metahack10",
                is_external=True),
        rx.text(f"protegiendo el activo más importante para las empresas, desde 2013 - {datetime.date.today().year}")
    )