import reflex as rx
from my_app_name.template.template import base_page

GLOBAL_BACKGROUND_COLOR = "#0F0F0F"
TEXT_COLOR_PRIMARY = "#F0F0F0"
TEXT_COLOR_SECONDARY = "#A0A0A0"

ACCENT_COLOR = "#FF6600"
ACCENT_COLOR_MUTED = "#E65C00"
ACCENT_COLOR_DARK = "#CC5200"
ACCENT_COLOR_SUBTLE = "#803300"

CARD_BG_COLOR = "rgba(25, 25, 25, 0.85)"
INFO_BOX_BG_COLOR = "rgba(35, 35, 35, 0.8)"
SECTION_BG_COLOR = "rgba(45, 45, 45, 0.75)"

HOVER_BG_COLOR = "rgba(60, 60, 60, 0.95)"

HERO_CARD_BG_COLOR_INNER = "radial-gradient(circle at center, rgba(20, 20, 20, 0.95), rgba(30, 30, 30, 0.98))"


@rx.page(route="/")
def home() -> rx.Component:
    return base_page(
        rx.container(
            rx.vstack(
                rx.vstack(
                    rx.image(
                        src="/icon.png",
                        width="120px",
                        height="auto",
                        border_radius="50%",
                        border=f"2px solid {ACCENT_COLOR_MUTED}",
                        box_shadow=f"0 0 18px {ACCENT_COLOR_SUBTLE}, 0 0 35px {ACCENT_COLOR_SUBTLE} inset",
                        margin_bottom="1.8em",
                        animation="fade-in-up 1.2s ease-out forwards, breathing-pulse 4s ease-in-out infinite",
                        object_fit="cover",
                    ),
                    rx.heading(
                        "S.K.Y.O.K.E.N.",
                        size="8",
                        color=ACCENT_COLOR,
                        weight="bold",
                        font_family="'Orbitron', sans-serif",
                        text_align="center",
                        text_shadow=f"0 0 18px {ACCENT_COLOR}, 0 0 35px {ACCENT_COLOR_MUTED}",
                        line_height="1.2",
                    ),
                    rx.text(
                        "System Development Engineer",
                        font_size="1.5em",
                        color=TEXT_COLOR_SECONDARY,
                        text_align="center",
                        max_width="700px",
                        padding_x="2em",
                        line_height="1.6",
                        letter_spacing="0.05em",
                        text_shadow="1px 1px 5px rgba(0,0,0,0.8)",
                        animation="fade-in-up 1.6s ease-out forwards",
                    ),
                    rx.flex(
                        rx.button(
                            "EXPLORE PROJECTS",
                            size="2",
                            color_scheme="orange",
                            on_click=lambda: rx.redirect("/archive"),
                            margin_right="2em",
                            padding="1.1em 2.5em",
                            border_radius="full",
                            box_shadow=f"0 0 10px {ACCENT_COLOR_SUBTLE}, 0 0 20px {ACCENT_COLOR_SUBTLE} inset",
                            _hover={
                                "box_shadow": f"0 0 20px {ACCENT_COLOR_MUTED}, 0 0 40px {ACCENT_COLOR_MUTED} inset",
                                "transform": "translateY(-5px) scale(1.05)",
                                "background": f"linear-gradient(to right, {ACCENT_COLOR}, {ACCENT_COLOR_DARK})",
                                "transition": "all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1)",
                                "color": "white",
                            },
                            animation="fade-in-up 1.8s ease-out forwards",
                        ),
                        rx.button(
                            "ABOUT ME",
                            size="2",
                            variant="outline",
                            color_scheme="orange",
                            on_click=lambda: rx.redirect("/about"),
                            padding="1.1em 2.5em",
                            border_radius="full",
                            box_shadow=f"0 0 8px {ACCENT_COLOR_SUBTLE}",
                            _hover={
                                "box_shadow": f"0 0 15px {ACCENT_COLOR_MUTED}, 0 0 30px {ACCENT_COLOR_SUBTLE}",
                                "transform": "translateY(-5px) scale(1.05)",
                                "background_color": HOVER_BG_COLOR,
                                "color": ACCENT_COLOR,
                                "transition": "all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1)",
                            },
                            animation="fade-in-up 2s ease-out forwards",
                        ),
                        margin_top="3em",
                        wrap="wrap",
                        justify="center",
                        align="center",
                        spacing="6",
                    ),
                    background=HERO_CARD_BG_COLOR_INNER,
                    padding="4em 3.5em",
                    border_radius="3xl",
                    border=f"1px solid {ACCENT_COLOR_SUBTLE}",
                    box_shadow=f"0 0 40px rgba(255,102,0,0.2), 0 0 80px rgba(255,102,0,0.1), inset 0 0 20px rgba(255,102,0,0.08)",
                    align="center",
                    width="100%",
                    max_width="1050px",
                    spacing="7",
                    position="relative",
                    overflow="hidden",
                ),
                spacing="0",
                align="center",
                min_height="100vh",
                padding_y="0",
                justify="center",
            ),
            background=GLOBAL_BACKGROUND_COLOR,
            max_width="100vw",
            height="100%",
            padding="0",
            margin="0",
            overflow="hidden",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content="center",
            position="relative",
        ),
        True
    )