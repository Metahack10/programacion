import reflex as rx
from App.componentes.title import title as title

def aportes() -> rx.Component:
    return rx.vstack(
        title("Aportes & Logros"),
        rx.box(
            rx.hstack(
                rx.box(
                    rx.text("Wpinger en Powershell"),
                    class_name = "box3"
                ),
                rx.box(
                    rx.text("TryHackMe Ranking"),
                    class_name = "box2"
                ),
                rx.box(
                    rx.text("Winrar Exploit (POC)"),
                    class_name = "box1"
                )
            ),
            rx.hstack(
                rx.box(
                    rx.text("Pinger en Bash"),
                    class_name = "box4"
                ),
                rx.box(
                    rx.text("HackBar"),
                    class_name = "box5"
                )
            )
        ),
        align_items = "start",
        spacing = "6",
        id = "Aportes"
    )