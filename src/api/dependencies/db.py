from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends

from infra.db.engine import session_maker
from persistence.utils import DBManager


def get_db_manager() -> DBManager:
    return DBManager(session_factory=session_maker)


async def get_db() -> AsyncGenerator[DBManager, None]:
    async with get_db_manager() as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
