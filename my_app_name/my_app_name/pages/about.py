# my_app_name/pages/about.py
import reflex as rx
from my_app_name.template.template import base_page
from my_app_name.ui.social_link import social_link

ABOUT_PAGE_BACKGROUND_COLOR = "black"
TEXT_COLOR_LIGHT = "white"
TEXT_COLOR_MEDIUM = rx.color("gray", 8)
ACCENT_COLOR = "orange"
RADIUS_COLOR = "white"

CARD_BG_COLOR = rx.color("gray", 3)
INFO_BOX_BG_COLOR = rx.color("gray", 2) 
SECTION_BG_COLOR = rx.color("gray", 1) 

COMMON_HOVER_STYLE = {
    "background_color": rx.color("gray", 5),
    "transform": "translateY(-5px)",
    "box_shadow": "lg",
    "cursor": "pointer",
}

COMMON_CARD_STYLE = {
    "width": "280px",
    "min_width": "280px",
    "height": "140px",
    "bg": CARD_BG_COLOR,
    "border_radius": "lg",
    "box_shadow": "md",
    "transition": "all 0.2s ease-in-out",
    "_hover": COMMON_HOVER_STYLE, 
}

SPACING_SM= "2" 
SPACING_MD = "4"  
SPACING_LG = "6" 
PADDING_SECTION = "3em" 

def project_card(title: str, skills: list[str], link: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.heading(
                    title,
                    size="4",
                    weight="bold",
                    color=TEXT_COLOR_LIGHT,
                    text_align="center",
                    white_space="normal",
                    word_break="break-word",
                    line_height="1.2",
                    flex_grow=0,
                    margin_bottom="0.2em",
                ),
                rx.text(
                    "Connect to Nintendo Switch over Bluetooth, to enable control, emulate amiibo and use script from the web.",
                    font_size="0.8em",
                    color=TEXT_COLOR_MEDIUM,
                    text_align="center",
                    white_space="normal",
                    word_break="break-word",
                    line_height="1.2",
                ),
                rx.flex(
                    *[
                        rx.badge(
                            skill,
                            color_scheme=ACCENT_COLOR,
                            variant="soft",
                            size="1",
                            margin="0.2em",
                            border_radius="full",
                        )
                        for skill in skills
                    ],
                    wrap="wrap",
                    justify="center",
                    align_items="center",
                    flex_grow=1,
                    width="100%",
                ),
                spacing="1",
                align_items="center",
                height="100%",
                justify_content="center",
            ),
            **COMMON_CARD_STYLE, 
            padding="0.8em", 
        ),
        href=link,
        is_external=True,
        text_decoration="none",
    )

def view_more_card(link: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.icon("arrow-right", size=60, color=ACCENT_COLOR),
                rx.heading(
                    "View More Projects",
                    size="5",
                    weight="bold",
                    color=TEXT_COLOR_LIGHT,
                    text_align="center",
                    white_space="normal",
                    word_break="break-word",
                    line_height="1.2",
                ),
                justify="center",
                align_items="center",
                height="100%",
                spacing="4",
            ),
            **COMMON_CARD_STYLE, 
            padding="1em", 
        ),
        href=link,
        is_external=True,
        text_decoration="none",
    )
def pet_card(name: str, birthday: str, gender: str, gender_icon: str, gender_color: str, image_src: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.avatar(
                src=image_src,
                border_radius="50%",
                border="2px solid "+RADIUS_COLOR,
                box_size="80px",
                transition="box-size 0.2s ease-in-out",
            ),
            rx.vstack(
                rx.text(
                    name,
                    font_size="1.5em",
                    weight="bold",
                    color=TEXT_COLOR_LIGHT,
                ),
                rx.hstack(
                    rx.icon("calendar", size=18, color=ACCENT_COLOR),
                    rx.text(birthday, font_size="0.9em", color=TEXT_COLOR_MEDIUM),
                    spacing="1",
                ),
                rx.hstack(
                    rx.icon(gender_icon, size=18, color=rx.color(gender_color, 9)),
                    rx.text(gender, font_size="0.9em", color=TEXT_COLOR_MEDIUM),
                    spacing="1",
                ),
                spacing="2",
                align_items="flex-start",
            ),
            spacing="4",
            align_items="center",
        ),
        width={"base": "100%", "sm": "calc(50% - 0.5em)", "md": "calc(33.33% - 0.5em)"},
        min_width="180px",
        height="auto",
        bg=rx.color("gray", 3),
        color=TEXT_COLOR_LIGHT,
        padding="1em",
        border_radius="lg",
        box_shadow="md",
    )

@rx.page(route="/about")
def about() -> rx.Component:
    return base_page(
        rx.box(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.avatar(
                            src="/image.png",
                            border_radius="50%",
                            border=f"1px solid {RADIUS_COLOR}",
                            box_size="150px",
                        ),
                        rx.heading(
                            "SKyoKen",
                            weight="bold",
                            font_family="MyFont",
                            font_size="4em",
                            color="white",
                        ),
                        align_items="center",
                        spacing=SPACING_MD, 
                    ),
                    rx.text(
                        "Major in information System Engineering.",
                        font_size="1.25em",
                        color=TEXT_COLOR_MEDIUM,
                        bg=INFO_BOX_BG_COLOR, 
                        text_align="center",
                        padding_x="2em",
                    ),
                    rx.center(
                        social_link("instagram", "/about", color=ACCENT_COLOR, size=25), 
                        social_link("twitter", "/about", color=ACCENT_COLOR, size=25), 
                        social_link("facebook", "/about", color=ACCENT_COLOR, size=25), 
                        social_link("linkedin", "/about", color=ACCENT_COLOR, size=25), 
                        social_link("github", "/about", color=ACCENT_COLOR, size=25), 
                        spacing=SPACING_SM, 
                        width="100%",
                    ),
                    spacing=SPACING_MD, 
                    align_items="center",
                    padding=PADDING_SECTION, 
                    width={"base": "100%", "md": "50%"},
                    justify_content="center",
                    border_radius="lg",
                    box_shadow="lg",
                    flex_grow=1,
                    flex_shrink=1,
                ),

                rx.vstack(
                    rx.hstack(
                        rx.icon("hand-metal", size=35, color=ACCENT_COLOR), 
                        rx.text("Skills & Projects", font_size="2em", weight="bold", color="white"),
                        align_items="center",
                        spacing=SPACING_SM, 
                        padding_left={"base": "1.5em", "md": "3em"},
                        width="100%",
                    ),
                    rx.flex(
                        project_card(
                            title="RasCon_NS",
                            skills=["Python", "Flask"],
                            link="https://github.com/SkyoKen/RasCon",
                        ),
                        view_more_card(link="https://github.com/SkyoKen"),
                        width="100%",
                        height="auto",
                        direction="row",
                        wrap="nowrap",
                        overflow_x="scroll",
                        padding_bottom="1em",
                        spacing=SPACING_MD, 
                        justify_content="center",
                        align_items="center",
                    ),
                    rx.divider(
                        color_scheme=ACCENT_COLOR, 
                        orientation="horizontal",
                        width="100%",
                        margin_x="auto",
                    ),
                    rx.hstack(
                        rx.icon("paw-print", size=35, color=ACCENT_COLOR), 
                        rx.text("My Pets", font_size="2em", weight="bold", color="white"),
                        align_items="center",
                        spacing=SPACING_SM, 
                        padding_left={"base": "1.5em", "md": "3em"},
                        width="100%",
                    ),
                    rx.flex(
                        pet_card(name="SUMI", birthday="2020-04-26", gender="FeMale", gender_icon="person_standing", gender_color="pink", image_src="/pet.png"),
                        pet_card(name="TACHI", birthday="2022-08-02", gender="Male", gender_icon="person_standing", gender_color="blue", image_src="/pet.png"),
                        pet_card(name="BANA", birthday="2022-08-02", gender="FeMale", gender_icon="person_standing", gender_color="pink", image_src="/pet.png"),
                        width="100%",
                        height="auto",
                        spacing=SPACING_SM, 
                        direction={"base": "column", "sm": "row"},
                        wrap="wrap",
                        justify="center",
                    ),
                    spacing=SPACING_LG,
                    align_items="flex-start",
                    padding=PADDING_SECTION, 
                    width={"base": "100%", "md": "50%"},
                    flex_grow=1,
                    flex_shrink=1,
                    bg=SECTION_BG_COLOR, 
                ),
                bg="black", 
                font_family="MyFont",
                spacing="0", 
                padding="0", 
                width="100%",
                height="100%",
                direction={"base": "column", "md": "row"},
                align_items="stretch",
            ),
            width="100vw",
            height="100%",
            padding="1em",
            display="flex",
            justify_content="center",
            align_items="center",
        )
    )