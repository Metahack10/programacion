import reflex as rx
from App.componentes.title import title as title

# def aportes() -> rx.Component:
#     return rx.vstack(
#         title("Aportes & Logros"),
#         rx.box(
#             rx.hstack(
#                 rx.box(
#                     rx.text("Wpinger en Powershell"),
#                     class_name = "box3"
#                 ),
#                 rx.box(
#                     rx.text("TryHackMe Ranking"),
#                     class_name = "box2"
#                 ),
#                 rx.box(
#                     rx.text("Winrar Exploit (POC)"),
#                     class_name = "box1"
#                 )
#             ),
#             rx.hstack(
#                 rx.box(
#                     rx.text("Pinger en Bash"),
#                     class_name = "box4"
#                 ),
#                 rx.box(
#                     rx.text("HackBar"),
#                     class_name = "box5"
#                 )
#             )
#         ),
#         align_items = "start",
#         spacing = "6",
#         id = "Aportes"
#     )

def aportes() -> rx.Component:
    return rx.vstack(
        title("Aportes & Logros"),
        rx.grid(
            rx.box(
                rx.text("Wpinger en Powershell"),
                class_name = "box3",
                grid_column = "1 / 2",
                grid_row = "1 / 2"
            ),
            rx.box(
                rx.text("TryHackMe Ranking"),
                class_name = "box2",
                grid_column = "2 / 3",
                grid_row = "1 / 2"
            ),
            rx.box(
                rx.text("Winrar Exploit (POC)"),
                class_name = "box1",
                grid_column = "3 / 4",
                grid_row = "1 / 3"
            ),
            rx.box(
                rx.text("Pinger en Bash"),
                class_name = "box4",
                grid_column = "1 / 2",
                grid_row = "2 / 3"
            ),
            rx.box(
                rx.text("HackBar"),
                class_name = "box5",
                grid_column = "2 / 3",
                grid_row = "2 / 3"
            ),
            template_columns = "repeat(3, 1fr)",
            template_rows = "repeat(2, auto)",
            gap = "10px"
        ),
        align_items = "start",
        spacing = "6",
        id = "Aportes"
    )