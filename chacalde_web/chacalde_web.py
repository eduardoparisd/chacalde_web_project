import reflex as rx

# Styles
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size

# Views
from chacalde_web.views.navbar import navbar
from chacalde_web.views.header import header

def index() -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.container(
            header(),
            bg="#eeff0d",
            height="85vh",
            max_width="900px",
            margin_y=Size.LARGE.value,
            padding_x=Size.BIG.value,
            border_radius=Size.LARGE.value,
        ),
        rx.container(
            
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
