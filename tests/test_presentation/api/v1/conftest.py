# ruff: noqa: E402

import os

from collections.abc import AsyncGenerator
from unittest import mock

import pytest

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

os.environ["ENV_FILE_NAME"] = ".test.env"

from config import SettingsModeEnum, settings
from infra.db import engine_null_pool, session_maker_null_pool
from persistence.models.base import BaseModel
from persistence.utils import DBManager, import_models
from presentation.api.v1.main import app
from presentation.api.v1.dependencies.db import get_db

import_models()

mock.patch(
    "fastapi_cache.decorator.cache",
    lambda *args, **kwargs: lambda f: f,  # noqa: ARG005
).start()


@pytest.fixture(scope="session", autouse=True)
async def check_test_mode() -> None:
    assert settings.mode == SettingsModeEnum.TEST


async def get_db_null_pool() -> AsyncGenerator[DBManager, None]:
    async with DBManager(session_maker_null_pool) as db:
        yield db


@pytest.fixture(scope="function", autouse=True)
async def db() -> AsyncGenerator[DBManager, None]:
    async for db in get_db_null_pool():
        yield db


app.dependency_overrides[get_db] = get_db_null_pool


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        transport = ASGITransport(app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode: None) -> None:  # noqa: ARG001
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
