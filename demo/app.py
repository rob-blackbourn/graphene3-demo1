"""The application
"""

from functools import partial
import os
from typing import Any, Mapping

from bareasgi import Application
from bareasgi_cors import CORSMiddleware
from bareasgi_graphql_next.graphene import add_graphene
from baretypes import (
    Scope,
    Info,
    Message
)
from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.bareclient import BareTweeterSession

from .schema import SCHEMA

APP_KEY = os.environ["APP_KEY"]
APP_KEY_SECRET = os.environ["APP_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


def make_application() -> Application:
    tweeter = Tweeter(
        BareTweeterSession(),
        # required for oauth1 signing:
        os.environ["APP_KEY"],
        os.environ["APP_KEY_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    )

    app = Application(
        info=dict(tweeter=tweeter),
        middlewares=[CORSMiddleware()]
    )

    add_graphene(
        app,
        SCHEMA
    )

    return app
