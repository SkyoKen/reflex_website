# my_app_name/template/template.py
import reflex as rx
from my_app_name.ui.navbar import navbar
from my_app_name.ui.footer import footer

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("404")

    return rx.vstack(
        # 导航栏
        navbar() if not hide_navbar else rx.box(),

        # 子页面内容容器
        rx.box(
            child,
            flex_grow=1, 
            width="100%",
        ),

        # 页脚
        footer() if not hide_navbar else rx.box(),

        # base_page
        width="100vw",
        min_height="100vh", 
        align_items="stretch",
        spacing="0", # 移除元素间的默认间距
        bg="transparent", # 确保这个 vstack 背景透明
    )