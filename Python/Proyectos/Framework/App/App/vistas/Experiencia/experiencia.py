import reflex as rx
from App.componentes.title import title as title
from App.estilos.styles import Size as Size
import App.estilos.styles as styles
from App.componentes.expe import expe

def experiencia() -> rx.Component:
    return rx.vstack(
        title("Experiencia"),
        expe("sofia_logo.jpeg", "Sofia Ltda.", "Jefe de Seguridad de la Información", "Implementación del SGSI | Analisis de Riesgos en Seguridad de la Información | Ethical Hacking"),
        expe("bec_logo.jpeg", "Banco Economico S.A.", "Encargado Nal. de Gestión de Seguridad de la Información y Riesgo Tecnológico", "Cumplimiento del RGSI de ASFI | Analisis de Riesgos en Seguridad de la Información | Ethical Hacking"),
        expe("bga_logo.jpeg", "Banco Ganadero S.A.", "Auditor de Riesgo Tecnológico", "Elaboración de Programs de Trabajo | Revisión de controles de gestión de TI | Revisión de procesos automatizados y aplicaciones"),
        align_items = "start",
        spacing = "6"
    )