from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import settings

engine = create_async_engine(settings.db.url)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

engine_null_pool = create_async_engine(settings.db.url, poolclass=NullPool)
session_maker_null_pool = async_sessionmaker(
    bind=engine_null_pool,
    expire_on_commit=False,
)
