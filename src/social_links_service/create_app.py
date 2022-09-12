import sys

from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from . import app
from .api.app_status import status_router

logger_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": "<level>level={level} {message}</level>",  # noqa
        }
    ]
}


def create_app():
    logger.configure(**logger_config)

    app.include_router(status_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
