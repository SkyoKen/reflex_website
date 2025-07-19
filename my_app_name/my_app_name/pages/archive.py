import reflex as rx
from my_app_name.template.template import base_page

TEXT_COLOR_LIGHT = "white"
TEXT_COLOR_MEDIUM = rx.color("gray", 8)
ACCENT_COLOR = "orange"
CARD_BG_COLOR = rx.color("gray", 3)
HOVER_BG_COLOR = rx.color("gray", 5)

# --- 公共悬停样式 ---
COMMON_HOVER_STYLE = {
    "background_color": HOVER_BG_COLOR,
    "transform": "translateY(-5px)",
    "box_shadow": "var(--shadow-6)",
    "cursor": "pointer",
    "z_index": "10", # 确保悬停时卡片浮在其他元素之上
}

# --- 作品数据 (实际项目中应从外部数据源加载，此处为示例数据) ---
PROJECTS = [
    {
        "title": "RasCon_NS",
        "description": "Connect to Nintendo Switch over Bluetooth, emulate amiibo and use script from the web.",
        "image": "/project.jpg",
        "link": "https://github.com/SkyoKen/RasCon_NS",
        "tags": ["Python", "Flask"],
        "is_placeholder": False,
    },
    # --- 占位项目 ---
    {
        "title": "Coming Soon",
        "description": "I'm currently compiling more exciting project examples, and they'll be updated soon!",
        "image": "/project.jpg",
        "link": "#",
        "tags": ["Coming Soon"],
        "is_placeholder": True,
    }
]

# --- 辅助函数：生成单个作品卡片组件 ---
def project_item_card(project: dict) -> rx.Component:
    """
    生成一个单独的作品项目卡片。
    根据 is_placeholder 属性调整样式和行为。
    """
    # 如果是占位项目，调整样式和行为
    if project.get("is_placeholder"):
        return rx.link(
            rx.card(
                rx.vstack(
                    rx.image(
                        src=project["image"],
                        height="180px",
                        width="100%",
                        object_fit="cover",
                        border_radius="lg",
                        border_bottom_radius="none",
                        alt=project["title"],
                        opacity="0.7", # 稍微降低透明度
                    ),
                    rx.vstack(
                        rx.heading(
                            project["title"],
                            size="5",
                            weight="bold",
                            color=TEXT_COLOR_LIGHT,
                            text_align="center", # 标题居中
                            width="100%",
                            margin_top="0.5em",
                        ),
                        rx.text(
                            project["description"],
                            font_size="0.9em",
                            color=TEXT_COLOR_MEDIUM,
                            text_align="center", # 描述居中
                            white_space="normal",
                            word_break="break-word",
                            line_height="1.4",
                            no_of_lines=2,
                            height="3em",
                        ),
                        rx.flex(
                            *[
                                rx.badge(
                                    tag,
                                    color_scheme=ACCENT_COLOR,
                                    variant="soft",
                                    size="1",
                                    margin="0.2em",
                                    border_radius="full",
                                    opacity="0.8",
                                )
                                for tag in project["tags"]
                            ],
                            wrap="wrap",
                            justify="center", # 标签居中
                            align_items="center",
                            width="100%",
                            margin_top="0.5em",
                        ),
                        spacing="2",
                        align_items="center", # 内部元素居中
                        width="100%",
                        padding_x="1em",
                        padding_bottom="1em",
                    ),
                    spacing="0",
                    align_items="center",
                    width="100%",
                    height="100%",
                ),
                width="320px",
                height="420px",
                bg=CARD_BG_COLOR,
                border_radius="lg",
                box_shadow="var(--shadow-3)", # 更浅的阴影
                _hover={
                    "background_color": rx.color("gray", 4),
                    "transform": "translateY(-3px)",
                    "box_shadow": "var(--shadow-4)",
                    "cursor": "pointer" if project["link"] != "#" else "default",
                },
                transition="all 0.15s ease-in-out",
                position="relative",
                border=f"1px dashed {TEXT_COLOR_MEDIUM}", 
            ),
            href=project["link"],
            is_external=(project["link"] != "#"),
            text_decoration="none",
            _hover={
                "text_decoration": "none",
            }
        )
    else:
        # 真实项目的卡片样式 (与之前相同)
        return rx.link(
            rx.card(
                rx.vstack(
                    rx.image(
                        src=project["image"],
                        height="180px",
                        width="100%",
                        object_fit="cover",
                        border_radius="lg",
                        border_bottom_radius="none",
                        alt=project["title"],
                    ),
                    rx.vstack(
                        rx.heading(
                            project["title"],
                            size="5",
                            weight="bold",
                            color=TEXT_COLOR_LIGHT,
                            text_align="left",
                            width="100%",
                            margin_top="0.5em",
                        ),
                        rx.text(
                            project["description"],
                            font_size="0.9em",
                            color=TEXT_COLOR_MEDIUM,
                            text_align="left",
                            white_space="normal",
                            word_break="break-word",
                            line_height="1.4",
                            no_of_lines=2,
                            height="3em",
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
                                for skill in project["tags"]
                            ],
                            wrap="wrap",
                            justify="start",
                            align_items="center",
                            width="100%",
                            margin_top="0.5em",
                        ),
                        spacing="2",
                        align_items="flex-start",
                        width="100%",
                        padding_x="1em",
                        padding_bottom="1em",
                    ),
                    spacing="0",
                    align_items="center",
                    width="100%",
                    height="100%",
                ),
                width="320px",
                height="420px",
                bg=CARD_BG_COLOR,
                border_radius="lg",
                box_shadow="var(--shadow-5)",
                _hover=COMMON_HOVER_STYLE,
                transition="all 0.15s ease-in-out",
                position="relative",
            ),
            href=project["link"],
            is_external=True,
            text_decoration="none",
            _hover={
                "text_decoration": "none",
            }
        )

@rx.page(route="/archive")
def archive() -> rx.Component:
    return base_page(
        rx.container(
            rx.vstack(
                # --- 作品网格展示区 ---
                rx.grid(
                    *[project_item_card(project) for project in PROJECTS],
                    columns={"base": "1", "sm": "2", "md": "3", "lg": "4"},
                    spacing="5",
                    gap="2em",
                    justify="center",
                    align_items="stretch",
                    width="100%",
                    padding_x={"base": "1em", "md": "0em"},
                    margin_x="auto",
                    max_width="1400px",
                ),

                spacing="8",
                align="center",
                min_height="85vh",
                padding_y="4em",
                justify="center",
            ),
            max_width="1400px",
            padding="2em",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content="center",
            height="100%",
        ),
    )