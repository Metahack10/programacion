import reflex as rx
from App.componentes.title import title as title
from App.estilos.colors import Color as Color


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
                class_name = "col1",
                width = "100%"
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
                class_name = "col2",
                width = "100%"
            ),
            rx.box(
                #rx.text("Proyecto Principal"),
                rx.link(
                    rx.heading(
                        "POC CVE-2323-38831",
                        size = "2",
                        color = Color.TITULO.value,
                        align = "center"
                    ),
                    rx.image(
                        src = "cve-2323-38831.jpg",
                        class_name = "laptop"
                    ),
                    href = "https://www.youtube.com/watch?v=LFzNChhzqns&t=6s",
                    is_external = True,
                    class_name = "linklap",
                    width = "100%"
                ),
                class_name = "col3",
                width = "100%"
            ),
            class_name = "container",
            width = "100%"
        ),
        width = "100%",
        align_items = "start",
        #spacing = "6",
        id = "Aportes"
    )