"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from my_app_name.pages.home import home
from my_app_name.pages.about import about
from my_app_name.pages.contact import contact
from my_app_name.pages.archive import archive

class State(rx.State):
    """The app state."""

app = rx.App(
    _state=State,
    stylesheets=[
        "/font/myfont.css",
    ],
)

app.add_page(home)
app._compile()
