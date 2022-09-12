import pathlib
import socket

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..settings import settings


class Engine:
    def __init__(self):
        working_dir = str(pathlib.Path().absolute().name)
        hostname = socket.gethostname()
        application_name = f"{working_dir} - {hostname}"
        url = URL.create(
            settings.postgres_driver,
            settings.postgres_user,
            settings.postgres_password,
            settings.postgres_host,
            settings.postgres_port,
            settings.postgres_database,
        )

        engine = create_async_engine(
            url=url,
            pool_size=5,
            pool_recycle=3600,
            connect_args={"server_settings": {"application_name": application_name}},
        )

        self.session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


engine = Engine()


async def get_engine() -> Engine:
    return engine
