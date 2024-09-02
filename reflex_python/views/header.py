import reflex as rx
import reflex_python.styles.styles as styles
from reflex_python.styles.styles import Size, TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de ADEViento 2024",
            size="lg",
            padding_top=Size.BIG.value,
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="mouredev.png",
                alt="Avatar de Brais Moure.",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.text("24 días. 24 regalos."),
                rx.text("Del 1 al 24 de diciembre."),
                rx.text(
                    "Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra "
                    "comunidad de developer!",
                    color=TextColor.ACCENT.value
                ),
                rx.text(
                    "Una actividad en la que cada día sortearé un regalo relacionado con programación "
                    "(libros, cursos, lo que sea)"
                ),
                rx.text(
                    "Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje de la comunidad"
                ),
                rx.link(
                    "#aDEViente 2024",
                    href="",
                    is_external=True,
                    color=TextColor.TERTIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                )
            ),
            flex_direction=["column", "column", "column", "row", "row"],
        ),
        padding_top= Size.VERY_BIG.value,
       style= styles.max_width_style,
    ),



