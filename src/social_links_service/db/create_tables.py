from sqlalchemy.engine.url import URL
from sqlmodel import SQLModel, create_engine

from ..settings import settings
from .sql_models import Communication, User, UserCommunication

url = URL.create(
    "postgresql+psycopg2",
    settings.postgres_user,
    settings.postgres_password,
    settings.postgres_host,
    settings.postgres_port,
    settings.postgres_database,
)
engine = create_engine(url=url)

SQLModel.metadata.create_all(engine)
