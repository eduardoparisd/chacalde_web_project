import reflex as rx

from enum import Enum

from .fonts import Fonts


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGX2 = "3em"
    VERY_BIG = "4em"
    PLUS1 = "5em"
    PLUS2 = "6em"
    PLUS3 = "7em"

# CDN STYLESHEETS
STYLES_SHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins&display=swap",
    "https://unpkg.com/nes.css@latest/css/nes.min.css"
]

# GLOBAL STYLES
BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "background_color": "#5a78f2",
    rx.Heading: {
        "font_family": Fonts.DEFAULT.value,
    }

}

# NAVBAR
navbar_styles = dict(
    position="sticky",
    padding_x=Size.BIG.value,
    padding_y=Size.SMALL.value,
    z_index="999",
    top="0",
    width="100%",
    #max_width="1100px",
    #border="5px solid green",
    border_bottom="0.25em solid white",
    display="flex",
    justify_content="space-evenly",
    align_content="center",
    _before={
        "content": "''",
        "position": "absolute",
        "top": "0",
        "right": "0",
        "bottom": "0",
        "left": "0",
        "background": "inherit",
        "opacity": "1",
        "backdrop_filter": "blur(10px)",
        "z_index": "-1"
    }
)

links_navbar_styles = dict(
    padding_x=Size.MEDIUM.value,
    padding_y=Size.DEFAULT.value,
    font_size=Size.DEFAULT.value,
    font_weight="bold",
    text_align="center",
    #text_decoration="none",
    color="#fff",
    background_color="#ff5252",
    border="3px solid #fff",
    border_radius="10px",
    box_shadow="5px 5px 0px #fff",
    transition="all 0.3 ease",
    cursor="",
    height=Size.LARGE.value,
    _hover={
        "background_color": "#fff",
        #"text_decoration": "none",
        "color": "#ff5252",
        "border": "3px solid #ff5252",
        "box_shadow": "5px 5px 0px #ff5252"
    }
)


# HEADER

header_heading_name = dict(
    background_color="#ff5252",
    border_radius="15px",
    width="100%",
    padding=Size.DEFAULT.value
)

header_grid_span = dict(
    background_color="#5a78f2",
    border_radius="17px",
    width="100%",
    padding_y=Size.MEDIUM.value,
    padding_x=Size.BIG.value,
    box_shadow="0 0 25px rgb(0,140,255)",
    backdrop_filter="blur(6px)",
    transition="all 0.5s",
    _hover={
        "border": "1px solid black",
        "transform": "scale(1.04)"
    },
)

header_grid_networks = dict(
    background_color="#6d6d6d",
    border_radius="17px",
    width="100%",
    padding_x=Size.DEFAULT.value,
    padding_top=Size.LARGE.value
    
)