import reflex as rx

PRIMARY_BG_COLOR = "black"
TEXT_COLOR = "white" 
ACCENT_COLOR = "orange" 


def navbar_images_menu_item(text: str, icon_path: str, url: str) -> rx.Component:
    """导航栏图片菜单项，适用于桌面和移动端。"""
    return rx.link(
        rx.text(
            text,
            size="4", 
            weight="medium",
            font_family="MyFont",
            color=TEXT_COLOR,
            _hover={
                "color": rx.color(ACCENT_COLOR, 9), 
                "text_decoration": "underline",
                "text_underline_offset": "4px", 
                "transition": "all 0.2s ease-in-out",
            },
        ),
        href=url,
        text_decoration="none", 
        padding_y="0.5em", 
        padding_x="1em",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2.5em", 
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SKyoKen",
                        size="8",
                        weight="bold",
                        font_family="MyFont",
                        color=TEXT_COLOR,
                    ),
                    align_items="center", 
                    spacing="3", 
                ),
                rx.hstack(
                    rx.button(
                        "Change Color",
                        on_click=rx.toggle_color_mode,
                    ),
                    navbar_images_menu_item("Home", "/icon.png", "/#"),
                    navbar_images_menu_item("Contact", "/icon.png", "/contact"),
                    navbar_images_menu_item("About", "/icon.png", "/about"),
                    navbar_images_menu_item("Archive", "/icon.png", "/archive"),
                    spacing="6",
                    align_items="center",
                ),
                justify="between",
                align_items="center", 
                padding_y="0.8em", 
                padding_x="2em", 
                width="100%", 
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SKyoKen",
                        size="7",
                        weight="bold",
                        font_family="MyFont",
                        color=TEXT_COLOR, 
                    ),
                    align_items="center",
                    spacing="3",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon(
                            "menu",
                            size=35, 
                            color=rx.color(ACCENT_COLOR, 9),
                            _hover={"color": rx.color(ACCENT_COLOR, 10)}, 
                        )
                    ),
                    rx.menu.content(
                        navbar_images_menu_item("Home", "/icon.png", "/#"),
                        rx.menu.separator(),
                        navbar_images_menu_item("Contact", "/icon.png", "/contact"),
                        rx.menu.separator(),
                        navbar_images_menu_item("About", "/icon.png", "/about"),
                        rx.menu.separator(),
                        navbar_images_menu_item("Archive", "/icon.png", "/archive"),
                        justify="center", 
                        bg=rx.color("black", 11),
                        border_color=rx.color(ACCENT_COLOR, 7), 
                        border_width="1px",
                        padding_y="1em",
                    ),
                    align_items="center",
                ),
                justify="between",
                align_items="center",
                padding="0.8em 1.5em",
                width="100%",
            ),
        ),
        bg=rx.color(PRIMARY_BG_COLOR), 
        padding_y="0.5em",
        width="100%", 
        position="sticky", 
        top="0px",
        z_index="5", 
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)", 
    )