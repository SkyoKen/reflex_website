import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"© {2025} SKyoKen. All rights reserved.",
            color=rx.color("white"), # 页脚文本为白色
            font_size="0.8em",
        ),
        padding="1em",
        bg=rx.color("black"), # 页脚背景设为黑色
        width="100%", # 确保占据整个宽度
        align_items="center", # 内容居中
    )