import reflex as rx
from App.componentes.link_button import link_button

def enlaces() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", 
                    "@mouredev", 
                    "https://twitch.tv/mouredev"),
        link_button("Youtube", 
                    "@Metahack", 
                    "https://www.youtube.com/@JorgeLopez-br4mt"),
        link_button("Github", 
                    "@Metahack", 
                    "https://github.com/Metahack10"),
        link_button("Twitter", 
                    "@Metahack", 
                    "https://x.com/Jlopez_life"),
        width="100%"
)