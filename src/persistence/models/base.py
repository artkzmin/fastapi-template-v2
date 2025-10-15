import uuid

from sqlalchemy import Integer, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    __abstract__ = True


class BaseUUIDModel(BaseModel):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )


class BaseStrIdModel(BaseModel):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        Text(),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )


class BaseIntIdModel(BaseModel):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
