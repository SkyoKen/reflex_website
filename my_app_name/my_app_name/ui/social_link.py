import reflex as rx
def social_link(icon: str,href: str, color="",size=25) -> rx.Component:
    if color == "":
        color = rx.color("accent", 10),
    return rx.link(
        rx.icon(
            icon,
            color = color,
            size=size,
            ), 
        href=href
        )