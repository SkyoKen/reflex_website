import reflex as rx
from rxconfig import config
from my_app_name.ui.social_link import social_link

def footer() -> rx.Component:
    return  rx.flex(
                rx.text(
                    "Copyright © SkyoKen Memo 2023",
                    size="3",
                    white_space="nowrap",
                    weight="medium",
                    font_family="MyFont"
                ),
                justify_content="center",
                width="100%",
            )