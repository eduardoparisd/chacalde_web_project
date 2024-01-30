import reflex as rx
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size
from chacalde_web.styles.colors import Color

def body() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Conoce mis Propuestas", 
            size="2xl",
            margin_top=Size.LARGE.value,
            margin_bottom=Size.SMALL.value
        ),
        rx.box(
            rx.span("""
                    Mi compromiso con nuestra comunidad me motiva a 
                    presentarles mis propuestas para la alcaldía. 
                    Creo firmemente que juntos podemos construir
                    un futuro vibrante y próspero para todos.
                    """,
                    style=styles.body_span_cards
            ),
            max_width="900px"
        ),
        rx.box(
            rx.hstack(
                rx.image(src="image_prop1.PNG",
                    h="100%",
                    width="55%"
                ),
                rx.span("""
                        Tapas de alcantarillas hechas con plástico reciclado y patrocinadas por empresas privadas. 
                        Generes un ingreso por publicidad y como son de plástico no se las roban.
                        """,
                        style=styles.body_span_cards
                ),
                style=styles.body_cards_style
            ),
            rx.hstack(
                rx.span("""
                        Un tram a travez de casco viejo hasta la central que decongestione el trafico, 
                        complemente el turismo y promueva el transporte colectivo.
                        """,
                        style=styles.body_span_cards
                ),
                rx.image(src="image_prop2.PNG",
                    h="100%",
                    width="55%",
                ),
                style=styles.body_cards_style
            ),
            rx.hstack(
                rx.image(src="image_prop3.PNG",
                        h="100%",
                        width="55%"
                        ),
                rx.span("""
                        Un app que permite a cualquiera poner una multa a un carro mal estacionado. 
                        Un funcionario confirma y emite la multa oficial.
                        """,
                        style=styles.body_span_cards
                ),
                style=styles.body_cards_style
            ),
            rx.hstack(
                rx.span("""
                        Zebras con leds que de noche parpadean pa advertirle a 
                        conductores que peatones están cruzando la calle.
                        """,
                        style=styles.body_span_cards
                ),
                rx.image(src="image_prop4.PNG",
                        h="100%",
                        width="55%"
                ),
                style=styles.body_cards_style
            ),
            rx.hstack(
                rx.image(src="image_prop5.PNG",
                        h="100%",
                        width="55%"
                    ),
                rx.span("""
                        Puente silvestre sobre el corredor norte para que la fauna pueda cruzar seguro.
                        """,
                        style=styles.body_span_cards
                ),
            style=styles.body_cards_style
            ),
            rx.hstack(
                rx.span("""
                        Un museo dentro de un galeón en el Causeway donde los 
                        turistas pueden aprender de Balboa y la historia de Panama.
                        """,
                        style=styles.body_span_cards
                ),
                rx.image(src="image_prop6.PNG",
                        h="100%",
                        width="55%"
                ),
                style=styles.body_cards_style
            ),
            margin_y=f"{Size.VERY_BIG.value} !important",
            border_radius="15px",
            background_color="#fff",
            padding_x=Size.PLUS1.value,
            max_width="1200px",
        ),
        bg=Color.SECONDARY_RED.value
    )