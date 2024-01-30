import reflex as rx
import chacalde_web.styles.styles as styles

from chacalde_web.styles.styles import Size
from chacalde_web.styles.colors import Color


def faq() -> rx.Component:
    return rx.vstack(
        rx.container(
            rx.heading(
            "Preguntas Frecuentes",
            size="2xl",
            bg=Color.SECONDARY_RED.value,
            margin_bottom=Size.MEDIUM.value,
            border_radius="15px",
            padding=Size.MEDIUM.value
            ),
            rx.accordion(
                rx.accordion_item(
                    rx.accordion_button(
                        rx.heading(
                            "¿Cuáles son los proyectos prioritarios que se llevarán a cabo durante el año 2024?",
                            size="sm"
                        ),
                        rx.spacer(),
                        rx.accordion_icon(),
                        padding_top=Size.MEDIUM.value
                    ),
                    rx.accordion_panel(
                        rx.text(
                            """
                            Durante el año 2024, nuestro enfoque estará en implementar proyectos estratégicos que 
                            aborden las necesidades más apremiantes de nuestra comunidad. 
                            Algunas de nuestras prioridades incluyen mejorar la infraestructura urbana, 
                            impulsar iniciativas de sostenibilidad, fortalecer la seguridad ciudadana y 
                            fomentar el desarrollo económico local. Estos proyectos serán cuidadosamente planificados y 
                            ejecutados en colaboración con la comunidad 
                            para asegurar un impacto positivo y sostenible.
                            """,
                        ),
                        style=styles.accordion_panel_style
                    ),
                    style=styles.accordion_item_style
                ),
                rx.accordion_item(
                    rx.accordion_button(
                        rx.heading(
                            "¿Cómo puedo participar y apoyar la campaña de Mayer Mizrachi?",
                            size="sm"    
                        ),
                        rx.spacer(),
                        rx.accordion_icon(),
                        padding_top=Size.MEDIUM.value
                    ),
                    rx.accordion_panel(
                        rx.text(
                            """
                            ¡Agradecemos tu interés en apoyar nuestra campaña! Hay varias formas de contribuir:
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text(
                            """
                            Únete como voluntario: Participa activamente en eventos, 
                            difusión en redes sociales y actividades locales.
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text(
                            """
                            Participa en eventos: Asiste a nuestras reuniones comunitarias, mítines y 
                            eventos para conocer más sobre nuestras 
                            propuestas y expresar tus ideas.
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text(
                            """
                            Tu apoyo es fundamental para construir un futuro sólido para nuestra ciudad. 
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text("¡Gracias por considerar unirte a nosotros!"),
                        style=styles.accordion_panel_style
                    ),
                    style=styles.accordion_item_style
                ),
                rx.accordion_item(
                    rx.accordion_button(
                        rx.heading(
                            "¿Cómo se llevarán a cabo las interacciones y la comunicación con la comunidad?",
                            size="sm"
                            ),
                        rx.spacer(),
                        rx.accordion_icon(),
                        padding_top=Size.MEDIUM.value
                    ),
                    rx.accordion_panel(
                        rx.text(
                            """
                            La transparencia y la comunicación abierta son fundamentales para nuestra administración. 
                            Planeamos implementar las siguientes medidas:
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text(
                            """
                            ◆ Sesiones regulares de participación ciudadana: Organizaremos reuniones periódicas para escuchar las inquietudes y sugerencias de la comunidad.
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text(
                            """
                            ◆ Plataformas en línea: Mantendremos una presencia activa en redes sociales y un sitio web actualizado para compartir información y recibir retroalimentación.
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text(
                            """
                            ◆ Oficina de atención al ciudadano: Estableceremos un punto de contacto físico donde los residentes puedan expresar sus inquietudes y recibir información. 
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text("◆ Informes regulares: Publicaremos informes periódicos sobre el progreso de proyectos y decisiones administrativas.",
                                margin_bottom=Size.MEDIUM.value,
                        ),
                        rx.text("Nos esforzaremos por construir un gobierno inclusivo y participativo, donde cada voz sea escuchada y cada opinión tenga un impacto significativo en la toma de decisiones."
                        ),
                        style=styles.accordion_panel_style
                    ),
                    style=styles.accordion_item_style
                ),

                rx.accordion_item(
                    rx.accordion_button(
                        rx.heading(
                            "¿Qué medidas tomará el candidato para promover la participación ciudadana?",
                            size="sm"
                            ),
                        rx.spacer(),
                        rx.accordion_icon(),
                        padding_top=Size.MEDIUM.value
                    ),
                    rx.accordion_panel(
                        rx.text(
                            """
                            Promover la participación ciudadana es esencial para una administración efectiva. 
                            Nuestras acciones incluirán:
                            """,
                            margin_bottom=Size.MEDIUM.value
                        ),
                        rx.text(
                            """
                            ◆ Creación de consejos comunitarios: Estableceremos grupos consultivos para abordar temas específicos y fomentar la participación activa.
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text(
                            """
                            ◆ Encuestas y consultas: Utilizaremos encuestas y consultas públicas para recopilar opiniones antes de tomar decisiones importantes.
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text(
                            """
                            ◆ Programas educativos: Implementaremos iniciativas para informar a la comunidad sobre los procesos gubernamentales y cómo pueden participar.
                            """,
                            margin_bottom=Size.SMALL.value
                        ),
                        rx.text("◆ Plataformas en línea: Facilitaremos la participación a través de plataformas digitales, permitiendo a los residentes expresar sus ideas y preocupaciones en línea.",
                                margin_bottom=Size.MEDIUM.value,
                        ),
                        rx.text("La participación ciudadana fortalece nuestra democracia y asegura que nuestras decisiones reflejen verdaderamente las necesidades y deseos de la comunidad que servimos."
                        ),
                        style=styles.accordion_panel_style
                    ),
                    style=styles.accordion_item_style
                ),

                allow_multiple=True,
                bg=Color.GREY.value,
                color="#fff",
                width="100%",
                border_radius="15px"
            ),
            bg=Color.TERTEARY_YELLOW.value,
            max_width="900px",
            padding_x=Size.BIG.value,
            padding_y=Size.BIG.value,
            border_radius=Size.LARGE.value,
        ),
        padding_y=Size.PLUS3.value,
        padding_x="12em",
    )