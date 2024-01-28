import reflex as rx

from chacalde_web.styles.styles import Size

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-medium",
        href=url,
        is_external=True,
        cursor="",
    )