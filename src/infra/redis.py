from typing import Self

from redis.asyncio import Redis

from config import settings
from logger import logger_app

logger = logger_app.getChild(__name__)


class RedisManager:
    redis: Redis

    def __init__(self, host: str, port: int, password: str) -> None:
        self._host: str = host
        self._port: int = port
        self._password: str = password

    async def __aenter__(self) -> Self:
        logger.info("Connecting to Redis")
        self.redis = Redis(host=self._host, port=self._port, password=self._password)
        await self.redis.ping()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: type | None,
    ) -> None:
        if self.redis:
            await self.redis.close()
            logger.info("Disconnecting from Redis")

    async def set(self, key: str, value: str, expire: int | None = None) -> None:
        await self.redis.set(key, value, ex=expire)

    async def get(self, key: str) -> bytes | None:
        return await self.redis.get(key)

    async def delete(self, key: str) -> None:
        await self.redis.delete(key)


redis_manager: RedisManager = RedisManager(
    host=settings.redis.host,
    port=settings.redis.port,
    password=settings.redis.password,
)
