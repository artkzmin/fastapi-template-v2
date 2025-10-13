import importlib

from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def import_models() -> None:
    importlib.import_module("persistence.models")


class DBManager:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory
        self._session: AsyncSession | None = None

    async def __aenter__(self) -> "DBManager":
        self._session = self._session_factory()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        session = self._get_session()
        await session.rollback()
        await session.close()

    async def commit(self) -> None:
        await self._get_session().commit()

    def _get_session(self) -> AsyncSession:
        """Return active session or raise if not initialized."""
        if self._session is None:
            raise RuntimeError("Session is not initialized")
        return self._session
