from sqlmodel import Field as sql_field
from sqlmodel import SQLModel


class User(SQLModel, table=True):
    """
    Модель Postgres-таблицы users.
    """

    __tablename__: str = "users"
    __table_args__ = {"extend_existing": True}
    id: int = sql_field(
        primary_key=True,
    )


class Communication(SQLModel, table=True):
    """
    Модель Postgres-таблицы communications.
    """

    __tablename__: str = "communications"
    __table_args__ = {"extend_existing": True}
    id: int = sql_field(
        primary_key=True,
    )


class UserCommunication(SQLModel, table=True):
    """
    Модель Postgres-таблицы users_communications.
    """

    __tablename__: str = "users_communications"
    __table_args__ = {"extend_existing": True}
    id: int = sql_field(
        primary_key=True,
    )
    communication_id: int = sql_field(foreign_key="communications.id")
    user_id: int = sql_field(foreign_key="users.id")
