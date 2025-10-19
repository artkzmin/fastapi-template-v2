from logger import setup_logging
from persistence.utils import check_db


async def setup_app() -> None:
    setup_logging()
    await check_db()
