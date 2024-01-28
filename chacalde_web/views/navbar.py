import reflex as rx 
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size


def navbar() -> rx.Component:
    return rx.hstack(
            rx.link(
                rx.image(
                    src="logo.PNG",
                    width=Size.BIGX2.value,
                    height=Size.BIGX2.value,
                    border_radius="5px",
                    margin_right=Size.MEDIUM.value
                ),
                "Chacalde",
                cursor="",
                font_weight="bold",
                display="flex",
                justify_content="space-between",
                align_items="center",
                _hover={
                    "text_decoration": "none"
                }
            ),
            rx.link(
                rx.button(
                "Inicio",
                style=styles.links_navbar_styles
                ),
                href="/"
            ),
            rx.link(
                rx.button(
                "Propuestas",
                style=styles.links_navbar_styles
                ),
                href="/"
            ),
            rx.link(
                rx.button(
                    "Alcaldía 2024",
                    style=styles.links_navbar_styles
                ),
                href="/"
            ),
            rx.link(
                rx.button(
                    "Únete",
                    style=styles.links_navbar_styles
                ),
                href="/"
            ),
            style=styles.navbar_styles
        )