import reflex as rx
from App.componentes.link_button import link_button

def enlaces() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://twitch.tv/mouredev"),
        link_button("Youtube", "https://www.youtube.com/@JorgeLopez-br4mt"),
        link_button("Github", "https://github.com/Metahack10"),
        link_button("Twitter", "https://x.com/Jlopez_life"),
        width="100%"
    )