import reflex as rx
from rxconfig import config
from my_app_name.template.template import base_page
@rx.page(route="/")
def home() -> rx.Component:
    return base_page(
        rx.container(rx.vstack(
            rx.hstack(
                rx.image(src="/icon.png", width="90px", height="auto"),
                rx.heading("home", size="9"),)
            ,
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        ),
    )