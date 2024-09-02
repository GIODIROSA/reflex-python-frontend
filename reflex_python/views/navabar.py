import reflex as rx
import reflex_python.constants as constans
from reflex_python.styles.styles import Size, Color
from reflex_python.components.link_icon import link_icon


def navbar()-> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.image(
            src="mouredev.png",
            alt="Imagen pixel art de MoureDev con estilo navideño",
            width= Size.VERY_BIG.value,
            height= Size.VERY_BIG.value
            ),
        rx.text("aDEViento 2024"),
        rx.spacer(),
        link_icon(
            "youtube",
            constans.YOUTUBE_URL
            ), 
         link_icon(
            "twitch",
            constans.TWITCH_URL
            ), 
          link_icon(
            "github",
            constans.GITHUB_URL
            ),
        width= "100%",
        display= "flex",
        align_items= "center"
        
    ),
        bg= Color.PRIMARY.value,
        position= "sticky",
        border_bottom= f"0.25em solid {Color.SECONDARY.value}",
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index= "999",
        top= "0",
        width= "100%"
    )

