import os

from enum import StrEnum
from pathlib import Path
from typing import Final

from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR: Final = Path(__file__).parent.parent
CONFIG_FILE_NAME: Final = os.getenv("ENV_FILE_NAME", ".env")
CONFIG_DIR: Final = BASE_DIR / "config"
ENV_PATH: Final = CONFIG_DIR / CONFIG_FILE_NAME


class SettingsModeEnum(StrEnum):
    TEST = "TEST"
    LOCAL = "LOCAL"
    DEV = "DEV"
    PROD = "PROD"


class SettingsServiceEnum(StrEnum):
    API_V1 = "API_V1"
    CLI = "CLI"


class Settings(BaseSettings):
    class ProjectSettings(BaseModel):
        name: str

    class APISettings(BaseModel):
        port: int
        workers: int

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
        password: str

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

    @property
    def is_local(self) -> bool:
        return self.mode == SettingsModeEnum.LOCAL

    @property
    def is_test(self) -> bool:
        return self.mode == SettingsModeEnum.TEST

    @property
    def is_prod(self) -> bool:
        return self.mode == SettingsModeEnum.PROD

    @property
    def is_dev(self) -> bool:
        return self.mode == SettingsModeEnum.DEV

    mode: SettingsModeEnum
    service: SettingsServiceEnum
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
        env_nested_delimiter=".",
    )


settings = Settings()
