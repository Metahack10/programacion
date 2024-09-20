import reflex as rx
from App.componentes.link_icon import link_cert
from App.componentes.title import title

def certificaciones() -> rx.Component:
    return rx.vstack(
        title("🏅Certificaciones"),
        rx.vstack(
            rx.flex(
                link_cert("https://cyberwarfare.live/product/multi-cloud-red-team-analyst-mcrta/", "MCRTA1.png"),
                rx.spacer(),
                link_cert("https://security.ine.com/certifications/ecppt-certification/", "eCPPT1.png"),
                rx.spacer(),
                link_cert("https://security.ine.com/certifications/ejpt-certification/", "eJPT1.png"),
                rx.spacer(),
                link_cert("https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/", "CEH1.png"),
                rx.spacer(),
                link_cert("https://www.comptia.org/es/certificaciones/security", "ComptiaSec+1.png"),
                width = "100%",
                gap = "20px",
                align = "center"
            )
            # rx.flex(
            #     link_cert("https://www.isc2.org/certifications/cc", "CC1.png"),
            #     rx.spacer(),
            #     link_cert("https://pecb.com/es/education-and-certification-for-individuals/iso-iec-27001/iso-iec-27001-lead-auditor", "ISO27001_1.png"),
            #     rx.spacer(),
            #     link_cert("https://pecb.com/es/education-and-certification-for-individuals/cybersecurity-management", "ISO27032_1.png"),
            #     rx.spacer(),
            #     link_cert("https://certiprof.com/es/products/scrum-master-professional-certificate-smpc?srsltid=AfmBOoqSPlldJzZq2tAusZiAkmkBw2KEgcYtpyIkusk9eBD6LukOCAmb", "SMPC1.png"),
            #     rx.spacer(),
            #     link_cert("https://www.scrumalliance.org/get-certified/product-owner-track/certified-scrum-product-owner", "CSPO1.png"),
            #     width = "80%"
            # )
        ),
        align_items = "start",
        spacing = "4"
)