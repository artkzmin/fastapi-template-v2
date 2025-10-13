import logging

from logging.config import dictConfig

from infra.config import settings


def setup_logging() -> None:
    settings.logs.dir_path.mkdir(parents=True, exist_ok=True)

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - trace_id=%(otelTraceID)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
                "access": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - trace_id=%(otelTraceID)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "INFO",
                },
                "file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "filename": f"{settings.logs.dir_path}/app.log",
                    "formatter": "default",
                    "level": "INFO",
                    "encoding": "utf-8",
                    "when": "midnight",
                    "backupCount": settings.logs.max_log_files,
                    "utc": True,
                },
                "access_file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "filename": f"{settings.logs.dir_path}/access.log",
                    "formatter": "access",
                    "level": "INFO",
                    "encoding": "utf-8",
                    "when": "midnight",
                    "backupCount": settings.logs.max_log_files,
                    "utc": True,
                },
            },
            "root": {
                "level": "INFO",
                "handlers": ["console", "file"],
            },
            "loggers": {
                "app": {
                    "level": "INFO",
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
                "uvicorn": {
                    "level": "INFO",
                    "handlers": ["console", "file"],
                    "propagate": True,
                },
                "uvicorn.error": {
                    "level": "INFO",
                    "handlers": ["console", "file"],
                    "propagate": True,
                },
                "uvicorn.access": {
                    "level": "INFO",
                    "handlers": ["console", "access_file"],
                    "propagate": True,
                },
                "httpcore.http11": {
                    "level": "INFO",
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
            },
        },
    )


logger_app = logging.getLogger(settings.project.name)
