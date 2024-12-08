import reflex as rx
from rxconfig import config

def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium",font_family="MyFont"),
        ),
        href=url,
    )


def navbar_icons_menu_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium",font_family="MyFont"),
        ),
        href=url,
    )
    
def navbar_images_menu_item(
    text: str, icon_path: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            # rx.image(icon_path, width="1.5em", height="auto"),
            rx.text(text, size="3", weight="medium",font_family="MyFont"),
        ),
        href=url,
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SKyoKen", size="7", weight="bold",font_family="MyFont"
                    ),
                    align_items="end",
                ),
                rx.hstack(
                        navbar_images_menu_item(
                            "Home", "/icon.png", "/#"
                        ),
                        navbar_images_menu_item(
                            "Contact", "/icon.png", "/contact"
                        ),
                        navbar_images_menu_item(
                            "About", "/icon.png", "/about"
                        ),
                        navbar_images_menu_item(
                            "Archive", "/icon.png", "/archive"
                        ),
                    spacing="6",
                align_items="end",
                ),
                justify="between",
                align_items="end",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SKyoKen", size="6", weight="bold",font_family="MyFont"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        navbar_images_menu_item(
                            "Home", "/icon.png", "/#"
                        ),
                        navbar_images_menu_item(
                            "Contact", "/icon.png", "/contact"
                        ),
                        navbar_images_menu_item(
                            "About", "/icon.png", "/about"
                        ),
                        navbar_images_menu_item(
                            "Archive", "/icon.png", "/archive"
                        ),
                    justify="end",
                ),
                    ),
                justify="between",
                align_items="center",
            ),
        ),
        background="center/cover url('/bg.jpg')",
        # bg=rx.color("sky", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )