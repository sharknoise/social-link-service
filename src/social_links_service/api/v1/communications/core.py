from collections import defaultdict
from statistics import mean

from loguru import logger
from sqlalchemy import select

from social_links_service.settings import settings

from ....codegen.models import (
    Communication,
    SendCommunicationResponse,
    SocialGraph,
    SocialLink,
    Statistics,
)
from ....db.postgres import Engine
from ....db.sql_models import Communication as DBCommunication
from ....db.sql_models import User, UserCommunication


async def send_communication_controller(
    body: Communication, engine: Engine
) -> SendCommunicationResponse:
    async with engine.session() as session:
        logger.info(f"Connecting to '{settings.postgres_database}' DB.")
        db_communication = DBCommunication()
        session.add(db_communication)
        await session.flush()
        for user_id in body.user_ids:
            user = User(id=user_id)
            await session.merge(user)
            await session.flush()
            user_communication = UserCommunication(
                communication_id=db_communication.id, user_id=user_id
            )
            session.add(user_communication)
            await session.flush()
        await session.commit()
    return SendCommunicationResponse(communication_id=db_communication.id)


async def get_social_graph_controller(engine: Engine) -> SocialGraph:
    async with engine.session() as session:
        communication_counts = defaultdict(lambda: 0)

        logger.info(f"Connecting to '{settings.postgres_database}' DB.")
        results = await session.execute(select(DBCommunication))
        for communication in results.scalars().all():
            results = await session.execute(
                select(UserCommunication).where(
                    UserCommunication.communication_id == communication.id
                )
            )
            user_communications = results.scalars().all()
            user_ids = frozenset(
                user_communication.user_id for user_communication in user_communications
            )
            communication_counts[user_ids] += 1
    social_links = []
    for user_ids, communication_count in communication_counts.items():
        social_links.append(
            SocialLink(user_ids=user_ids, communication_count=communication_count)
        )

    return SocialGraph(
        social_links=social_links,
        statistics=Statistics(
            minimum_communication_count=min(communication_counts.values()),
            maximum_communication_count=max(communication_counts.values()),
            average_communication_count=mean(communication_counts.values()),
        ),
    )
