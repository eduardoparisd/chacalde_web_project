import reflex as rx

# Styles
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size
from chacalde_web.styles.colors import Color

# Views
from chacalde_web.views.navbar import navbar
from chacalde_web.views.header import header
from chacalde_web.views.body import body
from chacalde_web.views.faq import faq

def index() -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.container(
            header(),
            bg=Color.TERTEARY_YELLOW.value,
            max_width="900px",
            margin_top=Size.BIG.value,
            margin_bottom=Size.PLUS1.value,
            padding_x=Size.BIG.value,
            border_radius=Size.LARGE.value,
        ),
        rx.fragment(
            body(),
            margin_y="20px !important"
        ),
        
        rx.fragment(
            faq()
        )
        
    )


# Create app instance and add index page.
app = rx.App(
    stylesheets=styles.STYLES_SHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Chacalde",
    description="Mayer Mizrachi y las propuestas a la alcaldía.",
    image="logo.PNG"
)
