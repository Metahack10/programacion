import reflex as rx
from App.componentes.link_icon import link_cert
from App.componentes.title import title

def certificaciones() -> rx.Component:
    return rx.vstack(
        title("Certificaciones Internacionales"),
        rx.vstack(
            rx.flex(
                link_cert("MCRTA","https://cyberwarfare.live/product/multi-cloud-red-team-analyst-mcrta/", "Certi/MCRTA.png", "Multi Cloud Red Team Analyst"),
                link_cert("eCPPT","https://security.ine.com/certifications/ecppt-certification/", "Certi/eCPPT.png", "elearn Certified Professional Penetration Tester"),
                link_cert("eJPT","https://security.ine.com/certifications/ejpt-certification/", "Certi/eJPT.png", "elearn Junior Penetration Tester"),
                link_cert("CEH","https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/", "Certi/CEH.png", "Certified Ethical Hacker"),
                link_cert("Comptia Sec+","https://www.comptia.org/es/certificaciones/security", "Certi/Comptia.png", "Comptia Security"),
                link_cert("Cybersecuty","https://www.isc2.org/certifications/cc", "Certi/CC.png", "Certified in Cybersecurity"),
                link_cert("ISO 27001","https://pecb.com/es/education-and-certification-for-individuals/iso-iec-27001/iso-iec-27001-lead-auditor", "Certi/ISO27001.png", "ISO 27001 Lead Auditor"),
                link_cert("ISO 27032","https://pecb.com/es/education-and-certification-for-individuals/cybersecurity-management", "Certi/ISO27032.png", "ISO 27032 Cybersecurity Lead Manager"),
                link_cert("SCMPC","https://certiprof.com/es/products/scrum-master-professional-certificate-smpc?srsltid=AfmBOoqSPlldJzZq2tAusZiAkmkBw2KEgcYtpyIkusk9eBD6LukOCAmb", "Certi/SMPC.png", "Scrum Master Professional Certificate"),
                link_cert("CSPO","https://www.scrumalliance.org/get-certified/product-owner-track/certified-scrum-product-owner", "Certi/CSPO.png", "Certified Scrum Product Owner"),
                width = "100%",
                align = "start",
                justify = "start",
                wrap = "wrap"
                
            )
            # rx.flex(
                
            #     width = "100%",
            #     align = "start",
            #     justify = "center",
            #     #align_items = "center",
            #     #justify_content = "center",
            #     margin_top = "10px",
            #     wrap = "wrap"
            # )
        ),
        align_items = "start",
        spacing = "4",
        id = "Certificaciones"
)