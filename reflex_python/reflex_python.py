
import reflex as rx
from rxconfig import config
import reflex_python.styles.styles as styles
from reflex_python.styles.styles import Size
from reflex_python.views.navabar import navbar
from reflex_python.views.header import header


class State(rx.State):
    """The app state."""
    ...


def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                width= "100%",
                align_items= "center",
                spacing= Size.VERY_BIG.value
            )
        )
        
    )


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style= styles.BASE_STYLE
)

app.add_page(
    index,
    title= "Calendario de aDEviento 2024 | 24 días. 24 regalos",
    description= "web python prueba | Giovanni Di Rosa | "
)

