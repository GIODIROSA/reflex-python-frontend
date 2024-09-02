import reflex as rx
import reflex_python.constants as constans
import reflex_python.styles.styles as styles
from reflex_python.styles.styles import Size, TextColor


def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de aDEViento 2024",
                font_size= Size.MEDIUM.value, 
                margin_bottom= Size.SMALL.value
            ),
            rx.link(
               "Creado con <3 (y gratis a ti) por Giovanni Di Rosa",
               font_size= Size.MEDIUM.value,
               color= TextColor.TERTIARY.value
              
            ),
            align_items="start",
            spacing= Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            alt="Logo moureDEv. Una letra \"eme\" entre dos corchetes.",
            class_name="nes-avatar is-large"
        ),
        padding_bottom= Size.BIG.value,
        style=styles.max_width_style
    )
    
