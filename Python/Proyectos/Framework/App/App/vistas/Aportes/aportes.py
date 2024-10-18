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
                        size = rx.breakpoints(initial = "1", sm = "1", lg = "2"),
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
                        size = rx.breakpoints(initial = "1", sm = "1", lg = "2"),
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
                        size = rx.breakpoints(initial = "1", sm = "2", lg = "3"),
                        class_name = "titulo2"
                    ),
                    rx.text(
                        "Level",
                        font_size = Size.DEFAULT.value,
                        text_align = "left",
                        color = Color.TITULO.value,
                        margin = "-7px 0 -10px 0",
                        padding = "2px"
                    ),
                    rx.text(
                        "Next Rank - Level 13 [GOD]",
                        font_size = Size.SMEDIUM.value,
                        text_align = "end",
                        color = Color.TITULO.value,
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
                        color = Color.TITULO.value,
                        margin = "-7px 0 -10px 0",
                        padding = "2px"
                    ),
                    rx.text(
                        "Fundamentals",
                        font_size = Size.SMEDIUM.value,
                        text_align = "start",
                        color = Color.TITULO.value,
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
                        color = Color.TITULO.value,
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
                        color = Color.TITULO.value,
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
                        color = Color.TITULO.value,
                        padding = "0 3px 0 0",
                        margin = "0 0 -12px 0"
                    ),
                    rx.progress(
                        value = 85,
                        width = "95%",
                        radius = "small",
                        height = "5px"
                    ),
                    href = "https://tryhackme.com/r/p/metahack10",
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
                    class_name = "row down2",
                    flex = rx.breakpoints(initial = "0.2", sm = "0.3", lg = "0.8")
                ),
                class_name = "col2",
                width = "100%"
            ),
            rx.link(
                rx.heading(
                    "POC WinRar CVE-2323-38831",
                    size = rx.breakpoints(initial = "2", sm = "4", lg = "6"),
                    class_name = "titulo"
                ),
                rx.image(
                    src = "logros/poc.png",
                    class_name = "img_poc",
                    height = rx.breakpoints(initial = "40%", sm = "50%", lg = "100%"),
                    width = rx.breakpoints(initial = "40%", sm = "50%", lg = "100%")
                ),   
                href = "https://www.youtube.com/watch?v=LFzNChhzqns&t=6s",
                class_name = "row col3",
                width = "100%",
                flex = rx.breakpoints(initial = "1.3", sm = "1.7", lg = "2.3"),
                is_external = True
            ),
            class_name = "container",
            height= rx.breakpoints(initial = "150px", sm = "300px", lg = "478px"),
            width = "100%"
        ),
        width = "100%",
        align_items = "start",
        spacing = "6",
        id = "Aportes",
    )