import os
import sys

from pathlib import Path

import uvicorn

os.environ["ENV_FILE_NAME"] = ".env"
sys.path.append(str(Path(__file__).parent))

from infra.config import settings
from infra.logger import setup_logging


def main() -> None:
    setup_logging()
    uvicorn.run("api.app:app", host="0.0.0.0", port=settings.api.port)


if __name__ == "__main__":
    main()
