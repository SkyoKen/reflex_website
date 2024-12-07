"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from my_app_name.pages.home import home
from my_app_name.pages.about import about
from my_app_name.pages.contact import contact
from my_app_name.pages.archive import archive

class State(rx.State):
    """The app state."""

    ...

app = rx.App(state=State,
        stylesheets=[  "/font/myfont.css",],
)
app.add_page(home)
app.add_page(about)
app.add_page(contact)
app.add_page(archive)
app._compile()