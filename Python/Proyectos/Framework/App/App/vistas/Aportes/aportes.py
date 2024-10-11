import reflex as rx
from App.componentes.title import title as title
from App.estilos.colors import Color as Color
from App.estilos.styles import Size as Size


def aportes() -> rx.Component:
    return rx.vstack(
        title("Aportes & Logros"),
        rx.box(
            rx.box(
                rx.link(
                    rx.heading(
                        "Wpinger en Powershell",
                        size = "2",
                        class_name = "titulo2"
                    ),
                    rx.image(
                        src = "logros/wpinger.svg",
                        class_name = "img_grid"
                    ),
                    href = "https://github.com/Metahack10/my_vault/tree/master/Powershell",
                    is_external = True,
                    class_name = "row up",
                ),
                rx.link(
                    rx.heading(
                        "Pinger en Bash",
                        size = "2",
                        class_name = "titulo2"
                    ),
                    rx.image(
                        src = "logros/pinger.svg",
                        class_name = "img_grid"
                    ),
                    href = "https://github.com/Metahack10/my_vault/tree/master/Bash",
                    is_external = True,
                    class_name = "row down"
                ),
                class_name = "col1",
                width = "100%"
            ),
            rx.box(
                rx.link(
                    rx.heading(
                        "TryHackMe Profile",
                        size = "3",
                        class_name = "titulo2"
                    ),
                    rx.text(
                        "Level",
                        font_size = Size.DEFAULT.value,
                        text_align = "left",
                        margin = "-7px 0 -10px 0",
                        padding = "2px"
                    ),
                    rx.text(
                        "Next Rank - Level 13 [GOD]",
                        font_size = Size.SMEDIUM.value,
                        text_align = "end",
                        padding = "0px 4px 0px 0px",
                        margin_bottom = "-10px"
                    ),
                    rx.progress(
                        value = 25,
                        variant = "surface",
                        color_scheme = "tomato",
                        radius = "small",
                        width = "95%",
                        height = "5px"
                    ),
                    rx.text(
                        "Skills",
                        font_size = Size.DEFAULT.value,
                        text_align = "left",
                        margin = "-7px 0 -10px 0",
                        padding = "2px"
                    ),
                    rx.text(
                        "Fundamentals",
                        font_size = Size.SMEDIUM.value,
                        text_align = "start",
                        padding = "0 3px 0 0",
                        margin = "0 0 -12px 0"
                    ),
                    rx.progress(
                        value = 100,
                        width = "95%",
                        radius = "small",
                        height = "5px"
                    ),
                    rx.text(
                        "Network Explotation",
                        font_size = Size.SMEDIUM.value,
                        text_align = "start",
                        padding = "0 3px 0 0",
                        margin = "0 0 -12px 0"
                    ),
                    rx.progress(
                        value = 95,
                        width = "95%",
                        radius = "small",
                        height = "5px"
                    ),
                    rx.text(
                        "Web Explotaition",
                        font_size = Size.SMEDIUM.value,
                        text_align = "start",
                        padding = "0 3px 0 0",
                        margin = "0 0 -12px 0"
                    ),
                    rx.progress(
                        value = 87,
                        width = "95%",
                        radius = "small",
                        height = "5px"
                    ),
                    rx.text(
                        "Linux",
                        font_size = Size.SMEDIUM.value,
                        text_align = "start",
                        padding = "0 3px 0 0",
                        margin = "0 0 -12px 0"
                    ),
                    rx.progress(
                        value = 85,
                        width = "95%",
                        radius = "small",
                        height = "5px"
                    ),
                    khref = "https://tryhackme.com/r/p/metahack10",
                    is_external = True,
                    class_name = "row up2"
                ),
                rx.link(
                    rx.heading(
                        "HackBar",
                        size = "1",
                        class_name = "titulo2"
                    ),
                    rx.image(
                        src = "logros/hackbar.svg",
                        class_name = "img_grid"
                    ),
                    href = "https://github.com/Metahack10/hack_statusbar",
                    is_external = True,
                    class_name = "row down2"
                ),
                class_name = "col2",
                width = "100%"
            ),
            rx.link(
                rx.heading(
                    "POC WinRar CVE-2323-38831",
                    size = "6",
                    class_name = "titulo"
                ),
                rx.image(
                    src = "logros/poc.png",
                    class_name = "img_poc"
                ),   
                href = "https://www.youtube.com/watch?v=LFzNChhzqns&t=6s",
                class_name = "row col3",
                width = "100%",
                is_external = True
            ),
            class_name = "container",
            width = "100%"
        ),
        width = "100%",
        align_items = "start",
        id = "Aportes"
    )