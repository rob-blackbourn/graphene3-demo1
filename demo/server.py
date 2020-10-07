"""The server
"""

import asyncio
import logging.config
import signal
from typing import Any, Mapping

from bareasgi import Application
import pkg_resources
import hypercorn.asyncio
import hypercorn.config

from demo.app import make_application

def start_server():
    """Start the server
    """
    logging.basicConfig(level=logging.DEBUG)

    app = make_application()

    config = hypercorn.config.Config()
    config.bind = ["0.0.0.0:10001"]
    config.loglevel = 'debug'

    asyncio.run(
        hypercorn.asyncio.serve(app, config)
    )

if __name__ == '__main__':
    start_server()
