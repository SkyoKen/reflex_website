import reflex as rx
from rxconfig import config
from my_app_name.ui.navbar import navbar
from my_app_name.ui.footer import footer


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("404")
    if hide_navbar:
        return rx.fragment(
            child,
            footer(),
        )
    return rx.fragment(
        navbar(),
        child,
        footer(),
    )
