import reflex as rx
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size
from chacalde_web.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "MAYER MIZRACHI MATALON", 
                size="2xl", 
                ),
            rx.heading("ALCALDE", size="xl"),
            style=styles.header_heading_name,
            #border="3px solid green"
        ),
        rx.grid(
            rx.grid_item(
                rx.image(
                    src="Captura2.PNG", 
                    width="100%", 
                    height="100%",
                    object_fit="cover",
                    display="block",
                    border_radius="15px",
                ),
                overflow="hidden",
                row_span=2, col_span=2
            ),
            rx.grid_item(
                rx.span(
                    """
                    Mayer Mizrachi un líder apasionado y comprometido, 
                    me postulo para la alcaldía con la firme convicción de 
                    llevar a nuestra comunidad hacia un futuro más brillante.
                    He demostrado la capacidad para tomar decisiones 
                    informadas y efectivas. Mi enfoque centrado en las personas y su historial de 
                    servicio comunitario le otorgan la experiencia necesaria para liderar nuestra ciudad.
                    """,
                    font_size="13px"
                ),
                style=styles.header_grid_span,
                row_span=1, col_span=3
            ),
            rx.grid_item(
                rx.center(
                    rx.heading("Sígueme en mis Redes Sociales", size="md"),
                    rx.spacer(),
                    rx.image(
                        src="logo.PNG",
                        width=Size.BIGX2.value,
                        height=Size.BIGX2.value,
                        border_radius="5px",
                    ),
                    margin_x=Size.BIG.value
                ),
                rx.center(
                    rx.hstack(
                        link_icon(
                            "instagram",
                            "https://www.instagram.com/mayermm/"
                        ),
                        rx.spacer(),
                        link_icon(
                            "close",
                            "https://twitter.com/Mayer"
                        ),
                        rx.spacer(),
                        link_icon(
                            "youtube",
                            "https://www.youtube.com/@Cerealistico"
                        ),
                        margin_top=Size.LARGE.value
                    )
                ),
                style=styles.header_grid_networks,
                row_span=1, col_span=3
            ),
            template_rows="repeat(2, 1fr)",
            template_columns="repeat(5, 1fr)",
            h="440px",
            width="100%",
            gap=5,
            padding_top=Size.MEDIUM.value,
        ),
        padding_y=Size.LARGE.value,
        height="100%", 
    )