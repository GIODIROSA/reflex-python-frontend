import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH= "1000px"

class Size(Enum):
    SMALL = "0.5em",
    MEDIUM = "0.8em"
    DEFAULT= "1em",
    BIG = "2em",
    VERY_BIG = "4em"
    

STYLESHEETS= [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" 
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}

max_width_style= dict(
   max_width= MAX_WIDTH,
   width= "100%",
)
  
