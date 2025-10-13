import os

from pathlib import Path
from typing import Final

from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from infra.config.enums import ModeEnum

BASE_DIR: Final = Path(__file__).parent.parent.parent.parent
CONFIG_FILE_NAME: Final = os.getenv("ENV_FILE_NAME", ".env")
CONFIG_DIR: Final = BASE_DIR / "config"
ENV_PATH: Final = CONFIG_DIR / CONFIG_FILE_NAME


class Settings(BaseSettings):
    class ProjectSettings(BaseModel):
        name: str

    class APISettings(BaseModel):
        port: int

    class DBSettings(BaseModel):
        host: str
        port: int
        user: str
        password: str
        name: str

        @property
        def url(self) -> str:
            return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    class RedisSettings(BaseModel):
        host: str
        port: int

    class LogsSettings(BaseModel):
        dir_path: Path
        max_log_files: int

        @field_validator("dir_path", mode="before")
        def resolve_dir_path(cls, v: str | Path) -> Path:
            return Path(v).resolve()

    class SecuritySettings(BaseModel):
        hash_key: str
        encrypt_key: str

    class ProxySettings(BaseModel):
        host: str
        port: int
        user: str
        password: str

        def is_configured(self) -> bool:
            return all([self.host, self.port, self.user, self.password])

        @property
        def socks5(self) -> str | None:
            if not self.is_configured():
                return None
            return f"socks5://{self.user}:{self.password}@{self.host}:{self.port}"

    mode: ModeEnum
    project: ProjectSettings
    api: APISettings
    db: DBSettings
    redis: RedisSettings
    logs: LogsSettings
    security: SecuritySettings
    proxy: ProxySettings

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="CONFIG__",
    )


settings = Settings()
