from fastapi import HTTPException, Response, status
from loguru import logger

from social_links_service.settings import settings

from ....codegen.models import (
    Communication,
    SendCommunicationResponse,
    SocialGraph,
    SocialLink,
    Statistics,
    UserIDs,
)
from ....db.postgres import Engine


async def send_communication_controller(body: Communication, engine: Engine) -> SendCommunicationResponse:
    return SendCommunicationResponse()


async def get_social_graph_controller(engine: Engine) -> SocialGraph:
    return SocialGraph()
