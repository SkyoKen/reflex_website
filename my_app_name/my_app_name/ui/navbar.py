import reflex as rx

PRIMARY_BG_COLOR = "#0F0F0F" 
TEXT_COLOR_PRIMARY = "#F0F0F0"
TEXT_COLOR_SECONDARY = "#A0A0A0"

ACCENT_COLOR = "#FF6600"
ACCENT_COLOR_MUTED = "#E65C00"
ACCENT_COLOR_DARK = "#CC5200"
ACCENT_COLOR_SUBTLE = "#803300"

HOVER_BG_COLOR = "rgba(60, 60, 60, 0.95)" 


def navbar_images_menu_item(text: str, icon_path: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            size="4",
            weight="medium",
            font_family="'Orbitron', sans-serif",
            color=TEXT_COLOR_PRIMARY,
            text_shadow=f"0 0 4px {ACCENT_COLOR_SUBTLE}",
        ),
        href=url,
        text_decoration="none", 
        padding_y="0.6em",
        padding_x="1em",
        border_radius="md",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2.4em",
                        height="auto",
                        border_radius="35%",
                        border=f"1px solid {ACCENT_COLOR_MUTED}",
                        box_shadow=f"0 0 8px {ACCENT_COLOR_SUBTLE}",
                    ),
                    rx.heading(
                        "SKYOKEN",
                        size="6",
                        weight="bold",
                        font_family="'Orbitron', sans-serif",
                        color=ACCENT_COLOR,
                        text_shadow=f"0 0 12px {ACCENT_COLOR}",
                    ),
                    align_items="center", 
                    spacing="3", 
                ),
                rx.hstack(
                    rx.icon(
                        tag="moon",
                        on_click=rx.toggle_color_mode,
                        size=40,
                        color=TEXT_COLOR_PRIMARY,
                        cursor="pointer",
                        padding="0.5em",
                        border_radius="full",
                        border=f"1px solid transparent",
                        _active={"border": f"1px solid {ACCENT_COLOR_MUTED}"}
                    ),
                    navbar_images_menu_item("Home", "/icon.png", "/#"),
                    navbar_images_menu_item("About", "/icon.png", "/about"),
                    navbar_images_menu_item("Archive", "/icon.png", "/archive"),
                    spacing="6",
                    align_items="center",
                ),
                justify="between",
                align_items="center", 
                padding_y="0.9em",
                padding_x="2.5em",
                width="100%", 
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="2.3em",
                        height="auto",
                        border_radius="35%",
                        border=f"1px solid {ACCENT_COLOR_MUTED}",
                        box_shadow=f"0 0 7px {ACCENT_COLOR_SUBTLE}",
                    ),
                    rx.heading(
                        "S.K.Y.O.K.E.N.",
                        size="7",
                        weight="bold",
                        font_family="'Orbitron', sans-serif",
                        color=ACCENT_COLOR,
                        text_shadow=f"0 0 8px {ACCENT_COLOR}",
                    ),
                    align_items="center",
                    spacing="2",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon(
                            "menu",
                            size=30,
                            color=ACCENT_COLOR,
                            border=f"1px solid {ACCENT_COLOR_MUTED}",
                            border_radius="md",
                            padding="0.25em",
                            box_shadow=f"0 0 4px {ACCENT_COLOR_SUBTLE}",
                        )
                    ),
                    rx.menu.content(
                        navbar_images_menu_item("Home", "/icon.png", "/#"),
                        rx.menu.separator(),
                        navbar_images_menu_item("About", "/icon.png", "/about"),
                        rx.menu.separator(),
                        navbar_images_menu_item("Archive", "/icon.png", "/archive"),
                        rx.menu.separator(),
                        rx.menu.item(
                            rx.icon(
                                tag="moon",
                                on_click=rx.toggle_color_mode,
                                size=28,
                                color=TEXT_COLOR_PRIMARY,
                                cursor="pointer",
                                width="100%",
                                text_align="center",
                                border=f"1px solid transparent",
                                _active={"border": f"1px solid {ACCENT_COLOR_MUTED}"}
                            ),
                            padding="0.5em 1em",
                        ),
                        justify="center", 
                        bg="rgba(15, 15, 15, 0.95)",
                        border_color=ACCENT_COLOR_MUTED,
                        border_width="1px",
                        padding_y="0.8em",
                        box_shadow=f"0 0 15px {ACCENT_COLOR_SUBTLE}",
                        border_radius="lg",
                    ),
                    align_items="center",
                ),
                justify="between",
                align_items="center",
                padding="0.8em 1.5em",
                width="100%",
            ),
        ),
        bg="linear-gradient(to right, rgba(15,15,15,0.95), rgba(30,30,30,0.95))",
        padding_y="0.7em",
        width="100%", 
        position="sticky", 
        top="0px",
        z_index="5", 
        box_shadow=f"0 4px 12px rgba(0, 0, 0, 0.4), 0 0 15px {ACCENT_COLOR_SUBTLE}",
        backdrop_filter="blur(4px)",
    )