"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
   
    
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, color="#2D3A27", size="4", weight="medium"), href=url)

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/ArmoniaA.png",
                        width="3.5em",
                        height="auto",
                        
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About us", "/#"),
                    navbar_link("Transfers", "/#"),
                    navbar_link("Tours", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button("Book a Tour", size="3"),
                    bg="#2D3A27",
                    color="#F2F0E4",
                    spacing="7",
                    justify="end",
                    border_radius="full",
                _hover={"bg": "#1A2518"}
                    
                ),
                bg="#F2F0E4",
                width="100%",
                padding_y="1.5em",
                padding_x="2em",
                justify="between",
                align_items="center"
                ),
        ),
        
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/ArmoniaA.png",
                        width="3em",
                        height="auto",
                        
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About us"),
                        rx.menu.item("Transfers"),
                        rx.menu.item("Tours"),
                        rx.menu.separator(),
                        rx.menu.item("Book a Tour"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
    
def hero_section() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(
                "ARMONIA\nEXCURSIONS",
                color="#2D3A27", 
                size="9", 
                line_height="1", 
                font_family="serif"
            ),
            rx.spacer(), 
            rx.text(
                "The most popular and trusted travel agency in Greece.",
                width="30%",
                color="#666",
                text_align="right",
                padding_bottom="1em"
            ),
            rx.spacer(),
            rx.link("EXPLORE DESTINATIONS ↗", href="#", font_weight="bold", margin_top="1em", color="black"),
            width="100%",
            align_items="end", # Alinea el texto pequeño con la base del título
            padding_y="3em",
        ),
        
        # FILA 2: La gran imagen de portada
        rx.image(
            src="/Grecia1.jpg", 
            width="100%",
            height="390px",
            object_fit="cover",
            border_radius="25px",
        ),
        bg = "#F2F0E4",
        width="100%",
    )
def about_and_benefits_section() -> rx.Component:
    return rx.vstack(
        # FILA 1: Diseño de 3 columnas (Imagen - Texto - Imagen)
        rx.flex(
            # Imagen Izquierda
            rx.box(
                rx.image(src="/Montana1.jpg", border_radius="20px", height="400px", object_fit="cover"),
                width="25%",
            ),
            # Texto Central
            rx.vstack(
                rx.text("✦ ABOUT US", color="gray", font_size="0.7em", letter_spacing="1px"),
                rx.heading("The Highest Level of Comfort and Service", color = "#2D3A27", size="8", font_family="serif"),
                rx.text(
                    "At Armonia Excursions, we combine premium service with attention to detail.",
                    color="#555"
                ),
                rx.link("MORE ABOUT US ↗", href="#", font_weight="bold", margin_top="1em", color="black"),
                width="40%",
                padding_x="3em",
                align_items="start",
                spacing="4",
            ),
            # Imagen Derecha
            rx.box(
                rx.image(src="/Pilar.jpg", border_radius="20px", height="550px", object_fit="cover"),
                width="35%",
            ),
            width="100%",
            align_items="center",
            padding_top="6em",
        ),

        # Espacio entre las fotos y los beneficios
        rx.spacer(height="4em"),
        rx.text("Why Choose Us?", color ="#2D3A27", font_size="1.5em", width="100%", text_align="left"),
        rx.divider(border_color="#ddd"),

        # FILA 2: Los beneficios en Grid
        rx.grid(
            rx.vstack(
                rx.heading("Professional team", size="4"),
                rx.text("With years of experience in tourism...", color="gray"),
                align_items="start",
            ),
            rx.vstack(
                rx.heading("Flexibility", size="4"),
                rx.text("From historic landmarks to airports and ports...", color="gray"),
                align_items="start",
            ),
            columns="2",
            spacing="9",
            width="100%",
            padding_y="3em",
        ),
        id="about", # ID para que el link de la Navbar funcione
        width="100%",
    )
def offer_practice_section() -> rx.Component:
    return rx.vstack(
        # 1. Títulos superiores
        rx.vstack(
            rx.heading("What we offer?", color ="#2D3A27", size="8"),
            rx.text(
                "From a private tour and a scheduled route to an accessible travel \n \n "
                "experience - we’ve got the perfect option for you"
                ),
            align_items="center",
            width="100%",
            margin_bottom="3em",
        ),

        # 2. El cuerpo de la sección (Las 3 columnas)
        rx.flex(
            # COLUMNA IZQUIERDA: Los "Botones" (en realidad son cajas de texto con estilo)
            rx.vstack(
                # Botón "Seleccionado" (Verde)
                rx.box(
                    rx.text("Private Tours", color="white"),
                    bg="#2D3A27", # Verde oscuro
                    padding="1.5em",
                    width="100%",
                    border_radius="10px",
                ),
                # Botones "No seleccionados" (Crema)
                rx.box(
                    rx.text("Scheduled Tours", color="black"),
                    bg="#E8E4D3", # Crema oscuro
                    padding="1.5em",
                    width="100%",
                    border_radius="10px",
                ),
                rx.box(
                    rx.text("Transfers", color="black"),
                    bg="#E8E4D3",
                    padding="1.5em",
                    width="100%",
                    border_radius="10px",
                ),
                width="25%", # Ocupa el primer cuarto
                spacing="3",
            ),

            # COLUMNA CENTRAL: La Imagen
            rx.box(
                rx.image(
                    src="/Trip.jpg", 
                    height="450px", 
                    width="100%", 
                    object_fit="cover", 
                    border_radius="15px"
                ),
                width="40%", # Un poco más ancha que las otras
                padding_x="2em",
            ),

            # COLUMNA DERECHA: El texto descriptivo
            rx.vstack(
                rx.text("✦ AS YOU WISH", color="gray", font_size="0.8em"),
                rx.heading("Tailored Private Tours", color = "#2D3A27", size="7"),
                rx.text(
                    "Enjoy a personalized journey in our Mercedes Vito (9-seater: 8 clients + driver) or minibus (14 seater: 13 clients + driver). \n These tours offer complete flexibility — visit as many or as few places as you wish, all at your own pace." 
                ),
                rx.button(
                    "EXPLORE TOURS ↗", 
                    variant="ghost", 
                    color="black", 
                    padding="0"
                ),
                width="35%",
                align_items="start", # Alineado a la izquierda
                spacing="4",
            ),

            width="100%",
            align_items="center", # Centra los 3 bloques verticalmente entre sí
        ),
        width="100%",
        padding_y="5em",
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar_buttons(),
        rx.vstack(
            hero_section(),
            about_and_benefits_section(),
            offer_practice_section(),
            max_width="1350px", # Esto lo hace ancho como la foto
            padding_x="40px",    # Espacio a los lados para que no toque el borde
            size="4"
            
        ),
        bg = "#F2F0E4",
        min_height="100vh",
    )
    


app = rx.App(
    style={
        "background_color": "#F2F0E4", 
        "font_family": "Instrument Sans, sans-serif",  
    }
)
app.add_page(index)
