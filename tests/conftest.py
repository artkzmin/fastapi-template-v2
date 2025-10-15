# ruff: noqa: E402

import os

from collections.abc import AsyncGenerator

import pytest

os.environ["ENV_FILE_NAME"] = ".test.env"

from app.db import DBManager
from app.setup import setup_app
from config import settings
from infra.db import engine_null_pool, session_maker_null_pool
from persistence.models.base import BaseModel
from persistence.utils import import_models

setup_app()
import_models()


@pytest.fixture(scope="session", autouse=True)
async def check_test_mode() -> None:
    assert settings.is_test


async def get_db_null_pool() -> AsyncGenerator[DBManager, None]:
    async with DBManager(session_maker_null_pool) as db:
        yield db


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode: None) -> None:  # noqa: ARG001
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
