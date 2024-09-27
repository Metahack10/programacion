import reflex as rx
from App.componentes.skill_icon import skill_icon
from App.componentes.title import title

def habilidades() -> rx.Component:
    return rx.vstack(
        title("Habilidades"),
        rx.box(
            rx.flex(
                skill_icon("skill/Kali-Linux.svg", "Kali Linux"),
                rx.spacer(),
                skill_icon("skill/Nmap.png", "Nmap Scanner"),
                rx.spacer(),
                skill_icon("skill/Metasploit.png", "Metasploit Framework"),
                rx.spacer(),
                skill_icon("skill/Bash.svg", "Bash Scripting"),
                rx.spacer(),
                skill_icon("skill/Powershell.svg", "Powershell Scripting"),
                rx.spacer(),
                skill_icon("skill/Python.svg", "Python"),
                rx.spacer(),
                skill_icon("skill/HTB.png", "HackTheBox"),
                rx.spacer(),
                skill_icon("skill/THM.png", "TryHackMe"),
                rx.spacer(),
                skill_icon("skill/VSCode.svg", "Visual Studio Code"),
                rx.spacer(),
                skill_icon("skill/Github.png", "GitHub"),
                rx.spacer(),
                skill_icon("skill/Notion.svg", "Notion"),
                
                #Esta parte es para repetir el Slider
                skill_icon("skill/Kali-Linux.svg", "Kali Linux"),
                rx.spacer(),
                skill_icon("skill/Nmap.png", "Nmap Scanner"),
                rx.spacer(),
                skill_icon("skill/Metasploit.png", "Metasploit Framework"),
                rx.spacer(),
                skill_icon("skill/Bash.svg", "Bash Scripting"),
                rx.spacer(),
                skill_icon("skill/Powershell.svg", "Powershell Scripting"),
                rx.spacer(),
                skill_icon("skill/Python.svg", "Python"),
                rx.spacer(),
                skill_icon("skill/HTB.png", "HackTheBox"),
                rx.spacer(),
                skill_icon("skill/THM.png", "TryHackMe"),
                rx.spacer(),
                skill_icon("skill/VSCode.svg", "Visual Studio Code"),
                rx.spacer(),
                skill_icon("skill/Github.png", "GitHub"),
                rx.spacer(),
                skill_icon("skill/Notion.svg", "Notion"),

                width = "100%",
                align_items = "center",
                justify_content = "center",
            ),
            class_name = "carrusel-contenido"
        ),
        align_items = "start",
        spacing = "4",
        class_name = "carrusel"
)