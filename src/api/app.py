from contextlib import asynccontextmanager
from typing import AsyncGenerator, Callable, Awaitable

from fastapi import FastAPI, Request, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource

from infra.logger import logger_app
from infra.redis.manager import redis_manager


LoggingInstrumentor().instrument(set_logging_format=True)
logger = logger_app.getChild(__name__)

resource = Resource(attributes={"service.name": "app"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    async with redis_manager:
        FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
        logger.info("FastAPI cache initialized")
        yield


app = FastAPI(lifespan=lifespan)
FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())


@app.middleware("http")
async def log_requests(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response
