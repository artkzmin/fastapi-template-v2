import importlib

from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def import_models() -> None:
    importlib.import_module("persistence.models")


class DBManager:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.session_factory: async_sessionmaker[AsyncSession] = session_factory
        self.session: AsyncSession | None = None

    async def __aenter__(self) -> "DBManager":
        self.session = self.session_factory()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        if self.session is not None:
            await self.session.rollback()
            await self.session.close()

    async def commit(self) -> None:
        if self.session is not None:
            await self.session.commit()
