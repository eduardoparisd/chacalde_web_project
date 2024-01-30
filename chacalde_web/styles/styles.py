import reflex as rx

from enum import Enum
from .fonts import Fonts
from chacalde_web.styles.colors import Color


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
    "background_color": Color.PRIMARY_BLUE.value,
    rx.Heading: {
        "font_family": Fonts.DEFAULT.value,
    },
    rx.Image: {
        "margin_x": Size.ZERO.value
    },
    rx.Span: {
        "margin_x": Size.ZERO.value
    },
    rx.Text: {
        "margin_bottom": Size.ZERO.value
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
    background_color=Color.SECONDARY_RED.value,
    border="3px solid #fff",
    border_radius="10px",
    box_shadow="5px 5px 0px #fff",
    transition="all 0.3 ease",
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
    background_color=Color.SECONDARY_RED.value,
    border_radius="15px",
    width="100%",
    padding=Size.DEFAULT.value
)

header_grid_span = dict(
    background_color=Color.PRIMARY_BLUE.value,
    border_radius="17px",
    width="100%",
    padding_y=Size.MEDIUM.value,
    padding_x=Size.BIG.value,
    transition="all 0.5s"
)

header_grid_networks = dict(
    background_color=Color.GREY.value,
    border_radius="17px",
    width="100%",
    padding_x=Size.DEFAULT.value,
    padding_top=Size.LARGE.value
    
)

# BODY

body_cards_style = dict(
    background_color="#c2cdfb",
    #AGREGAR EL COLOR 232385 A COLORS.
    color="#232385",
    overflow="hidden",
    border_radius="20px",
    h="14em",
    margin_y=Size.BIGX2.value,
    transition="all 0.5s",
    cursor="",
    _hover={
        "box_shadow": "0 0 25px rgb(0,140,255)",
        "backdrop_filter": "blur(6px)",
        "transform": "scale(1.02)"
    },
)

body_span_cards = dict(
    display="block",
    text_align="center",
    padding_x=Size.BIGX2.value,
    width="100%"
)

# FAQ 
accordion_item_style = dict(
    padding_y=Size.MEDIUM.value,
    padding_x=Size.LARGE.value
)

accordion_panel_style = dict(
    text_align="justify",
    margin_top=Size.SMALL.value,
    font_size=Size.MEDIUM.value
)