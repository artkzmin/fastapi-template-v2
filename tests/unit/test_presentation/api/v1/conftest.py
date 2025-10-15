# ruff: noqa: E402

import os

from collections.abc import AsyncGenerator
from unittest import mock

import pytest

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

os.environ["ENV_FILE_NAME"] = ".test.env"

from infra.db import session_maker_null_pool
from persistence.utils import DBManager, import_models
from presentation.api.v1.dependencies.db import get_db
from presentation.api.v1.main import app

import_models()

mock.patch(
    "fastapi_cache.decorator.cache",
    lambda *args, **kwargs: lambda f: f,  # noqa: ARG005
).start()


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
