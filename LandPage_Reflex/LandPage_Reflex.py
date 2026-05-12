"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    @rx.event
    def registro_free(self):
        return rx.window_alert("Iniciando registro: Sign up free")

    @rx.event
    def start_jiving(self):
        return rx.window_alert("¡Empezando la experiencia: Start jiving!")

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/PNGJIVE.png", height="2em"), 
        rx.spacer(),
        rx.hstack(
            rx.button("Log in", variant="ghost"),
            rx.button(
                "Sign up free", 
                on_click=State.registro_free,
                bg="black", color="white", border_radius="full",
                padding_x="1.5em"
            ),
            spacing="4",
        ),
        width="100%",
        padding="1.5em 10%",
        position="fixed",
        top="0",
        z_index="1000",
        bg="rgba(255, 255, 255, 0.8)",
        backdrop_filter="blur(10px)",
    )

def hero_section() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.image(
                src="/FondoRayasTran.png",
                width="100vw",
                height="auto",
                opacity="0.6",
            ),
            rx.vstack(
                rx.heading(
                    "Don't make connecting awkward", 
                    size="9", 
                    text_align="center",
                    max_width="800px",
                    margin_top="2em"
                ),
                rx.text("No more fumbling for business cards.", color="gray"),
                rx.image(
                    src="/CELULAR.png",
                    width="450px",
                    height="auto",
                    margin_top="2em",
                ),
                rx.button(
                    "Sign up free", 
                    on_click=State.registro_free,
                    bg="black", color="white", 
                    size="4", border_radius="full",
                    padding="1.5em 2.5em",
                    margin_top="2em"
                ),
                align_items="center",
                spacing="5",
            ),
            width="100%",
        ),
        width="100%",
        padding_top="6em",
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.vstack(
            hero_section(),

        ),
    )


app = rx.App()
app.add_page(index)
