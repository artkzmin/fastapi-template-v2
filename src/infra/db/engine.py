from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from infra.config import settings

engine = create_async_engine(settings.db.url)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
