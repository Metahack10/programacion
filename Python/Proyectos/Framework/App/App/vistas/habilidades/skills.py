import reflex as rx
from App.componentes.skill_icon import skill_icon
from App.componentes.title import title

def habilidades() -> rx.Component:
    return rx.vstack(
        title("Habilidades"),
        rx.box(
            rx.flex(
                skill_icon("skill/Kali-Linux.svg"),
                rx.spacer(),
                skill_icon("skill/Nmap.png"),
                rx.spacer(),
                skill_icon("skill/Metasploit.png"),
                rx.spacer(),
                skill_icon("skill/Bash.svg"),
                rx.spacer(),
                skill_icon("skill/Powershell.svg"),
                rx.spacer(),
                skill_icon("skill/Python.svg"),
                rx.spacer(),
                skill_icon("skill/HTB.png"),
                rx.spacer(),
                skill_icon("skill/THM.png"),
                rx.spacer(),
                skill_icon("skill/VSCode.svg"),
                rx.spacer(),
                skill_icon("skill/Github.png"),
                rx.spacer(),
                skill_icon("skill/Notion.svg"),
                width = "100%",
                align_items = "center",
                justify_content = "center"
            ),
            class_name = "carousel-container"
        ),
        align_items = "start",
        spacing = "4"
)