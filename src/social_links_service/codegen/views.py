# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2022-09-13T15:02:06+00:00

from __future__ import annotations

from typing import Union

from fastapi import Depends

from ..api.v1.communications.core import (
    get_social_graph_controller,
    send_communication_controller,
)
from ..db.postgres import Engine, get_engine
from .main import app
from .models import (
    Communication,
    HTTPValidationError,
    SendCommunicationResponse,
    SocialGraph,
)


@app.get(
    '/api/v1/communications',
    response_model=SocialGraph,
    tags=['Communications'],
    summary="Получить гиперграф социальных связей",
)
async def get_social_graph_view(engine: Engine = Depends(get_engine)) -> SocialGraph:

    return await get_social_graph_controller(engine)


@app.post(
    '/api/v1/communications/send',
    response_model=SendCommunicationResponse,
    tags=['Communications'],
    summary="Отправить информацию о факте коммуникации",
)
async def send_communication_view(
    body: Communication, engine: Engine = Depends(get_engine)
) -> SendCommunicationResponse:

    return await send_communication_controller(body, engine)
