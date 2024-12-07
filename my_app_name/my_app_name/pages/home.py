import reflex as rx
from rxconfig import config
from my_app_name.template.template import base_page
    
@rx.page(route="/")
def home() -> rx.Component:
    return base_page(
        rx.container(
        rx.vstack(
            rx.hstack(
                rx.image(src="/icon.png", width="90px", height="auto"),
                rx.heading("窝滴小网页~", size="9"),)
            ,
            rx.text(
                "窝滴小网页是一个基于",
                rx.code(f"Reflex"),
                "框架的示例应用。",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        ),
    )