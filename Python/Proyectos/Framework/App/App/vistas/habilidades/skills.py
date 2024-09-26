import reflex as rx
from App.componentes.skill_icon import skill_icon
from App.componentes.title import title

def habilidades() -> rx.Component:
    return rx.vstack(
        title("Habilidades"),
        rx.hstack(
            rx.flex(
                skill_icon("Nmap", "Nmap1.png"),
                rx.spacer(),
                skill_icon("Metasploit", "skill/Metasploit.png"),
                #rx.spacer(),
                #skill_icon("eJPT", "eJPT1.png"),
                #rx.spacer(),
                #skill_icon("CEH", "CEH1.png"),
                #rx.spacer(),
                #skill_icon("Comptia Sec+", "ComptiaSec+1.png"),
                width = "100%",
                align_items = "center",
                justify_content = "center"
            )
        ),
        align_items = "start",
        spacing = "4"
)