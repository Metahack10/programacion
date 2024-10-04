import reflex as rx
from App.componentes.title import title as title


def aportes() -> rx.Component:
    return rx.vstack(
        title("Aportes & Logros"),
        rx.box(
            rx.box(
                rx.box(
                    rx.text("Proyecto # 3"),
                    class_name = "row up",
                ),
                rx.box(
                    rx.text("Proyecto # 4"),
                    class_name = "row down"
                ),
                class_name = "col1"
            ),
            rx.box(
                rx.box(
                    rx.text("Proyecto # 2"),
                    class_name = "row up2"
                ),
                rx.box(
                    rx.text("Proyecto # 5"),
                    class_name = "row down2"
                ),
                class_name = "col2"
            ),
            rx.box(
                rx.text("Proyecto Principal"),
                class_name = "col3"
            ),
            class_name = "container",
        ),
        align_items = "start",
        spacing = "6",
        id = "Aportes"
    )