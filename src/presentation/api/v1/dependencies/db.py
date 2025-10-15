from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends

from app.db import DBManager, get_db_manager


async def get_db() -> AsyncGenerator[DBManager, None]:
    async with get_db_manager() as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
