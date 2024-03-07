import streamlit as st
import streamlit_shadcn_ui as ui

layout = "centered"
page_title = "Portfolio| Jorge (Metahack10)"
Page_icon = "🥷"

# --- VARIABLES ---
name = "Jorge Lopez (Metahack)"
descripcion = "Ingeniero Informático con especialización en Seguridad de la Información y Hacking Ético, soy una persona metódica y ordenada que siempre anda en busqueda de nuevos retos."
cvfile = "assets/Curriculum Vitae JL.pdf"
css_file = "styles/main.css"
cvname = "CV_JorgeLopez.pdf"
fotoperfil = "assets/perfil.jpg"

social_media = {
    "YouTube": "https://www.youtube.com/channel/UCHQLT6a-x9c4mtxj_EF5wlg",
    "LinkedIn": "https://www.linkedin.com/in/jorge-lopez-vicente/",
    "GitHub": "https://github.com/Metahack10?tab=repositories",
}
proyectos = {
    "📌 Barra de estados Hack para Kali Linux": "https://github.com/Metahack10/hack_statusbar",
    "📌 Script para hacer barrido de ping en bash": "https://github.com/Metahack10/my_vault/tree/master/Bash",
    "📌 Scripts para explotar Buffer Overflow": "https://github.com/Metahack10/my_vault/tree/master/Buffer",
}

#---CONF PAGINA ---
st.set_page_config(page_title=page_title, page_icon=Page_icon, layout=layout)

#Vincula la hoja de estilos CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#Lee el pdf del CV
with open(cvfile, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- LINKS REDES SOCIALES ---
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn_{platform}")

# --- CABECERA ---
col1, col2 = st.columns(2)
with col1:
    st.image(fotoperfil, width=300)
with col2:
    st.title(name)
    st.write(descripcion)
    st.download_button(label=" 📄 Descargar CV", data=PDFbyte, file_name=cvname)

# --- PROYECTOS ----
st.write("##")
st.subheader("Proyectos")
st.write("---")

for project, link in proyectos.items():
    st.write(f"[{project}]({link})")

# --- HABILIDADES ----
st.write("##")
st.subheader("Habilidades")
st.write("---")
st.write(
    """
- 🗂️ Gestión: Elaboración de políticas y procedimientos de seguridad de la información, implementación de estándares y frameworks de seguridad, como: ISO 27002, PCI-DSS, CIS Control, NIST
- 🛠️ Menejo de Herramientas: Nessus Scanner, OwaspZap, Nmap, BurpSuite, Acunetix, Guardium IBM, Novasec GRC, Metasploit, Monday, Smartfense
- 💻 Análisis de Vulnerabilidades: entornos de infraestructura (dispositivos de red, servidores y endpoints), aplicaciones web, aplicaciones móviles
- 🖥️ Programación: Bash, Python, Visual Basic para Excel
"""
)

# --- EXPERIENCIA ---
st.write("##")
st.subheader("Experiencia")
st.write("---")

#Trabajo 1
st.write("💼", "**Jefe de Seguridad de la Información**")
empresa = "Avicola Sofia Ltda."
enlace = "https://sofia.com.bo/"

st.write("Empresa: ",f"[{empresa}]({enlace})") 
st.image("assets/sofia.png",width=50)
st.write("👥 Empleados: 1000 - 5000")
st.write("05/2021 - Presente")
st.write(
    """
▶️ Análisis de riesgos de seguridad de la información\n
▶️ Implementación, monitoreo y mantenimiento de un sistema de gestión de seguridad de la información\n
▶️ Gestión de incidentes de seguridad de la información\n
▶️ Ethical Hacking a proyectos y sistemas internos
"""
)

#Trabajo 2
st.write("💼", "**Encargado Nal. de Gestión de Seguridad de la Información y Riesgo Tecnológico**")
empresa = "Banco Económico S.A."
enlace = "https://www.baneco.com.bo/"

st.write("Empresa: ",f"[{empresa}]({enlace})") 
st.image("assets/baneco.jpg",width=40)
st.write("👥 Empleados: 1000 - 5000")
st.write("02/2019 - 05/2021")
st.write(
    """
▶️ Análisis de riesgos de seguridad de la información\n
▶️ Implementación y mantenimiento del reglamento para la gestión de seguridad de la información de ASFI\n
▶️ Gestión de incidentes de seguridad de la información\n
▶️ Capacitación en temas de seguridad a personal interno
"""
)

#Trabajo 3
st.write("💼", "**Auditor de Sistemas**")
empresa = "Banco Económico S.A."
enlace = "https://www.baneco.com.bo/"

st.write("Empresa: ",f"[{empresa}]({enlace})") 
st.image("assets/baneco.jpg",width=40)
st.write("👥 Empleados: 1000 - 5000")
st.write("04/2015 - 02/2019")
st.write(
    """
▶️ Elaborar programas de auditoria de sistemas\n
▶️ Revisar y evaluar los controles de continuidad y seguridad de la información\n
▶️ Auditar la gestión de tecnologías de la información en la empresa\n
▶️ Revisar el correcto desempeño de los sistemas internos de la empresa
"""
)

#Trabajo 4
st.write("💼", "**Auditor de Riesgo Tecnológico**")
empresa = "Banco Ganadero S.A."
enlace = "https://www.bg.com.bo/personas/"

st.write("Empresa: ",f"[{empresa}]({enlace})") 
st.image("assets/bga.png",width=80)
st.write("👥 Empleados: 1000 - 5000")
st.write("10/2013 - 03/2015")
st.write(
    """
▶️ Auditar el cumplimiento del reglamento para la gestión de seguridad de la información de ASFI\n
▶️ Participar en la ejecución de las pruebas del Plan de Contingencias Tecnológico y Continuidad del Negocio\n
▶️ Implementar auditorias continuas mediante revisiones automatizadas a procesos recurrentes\n
▶️ Revisar el correcto desempeño de los sistemas internos de la empresa
"""
)