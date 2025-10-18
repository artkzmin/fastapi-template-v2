# FastAPI Application Template

## Архитектура
Архитектура проекта описана в [docs/ARCHITECTURE.md](docs/ARCHITECTURE.MD).

## Creds
Для запуска требуется файл с переменными окружения:
```bash
cp config/.env.dist config/.env
cp config/.test.env.dist config/.test.env
```

## Pre Commit
На проект установлен Pre Commit для единого стиля (используются `mypy`, `ruff`, `black`).
Для проверки и форматирования удобно пользоваться командой:
```bash
make format
```

## Зависимости и `uv`
Для управления зависимостями используются команды uv:
- `uv add PACKAGE_NAME` - добавление пакета;
- `uv remove PACKAGE_NAME` - удаление пакета;
- `uv sync` - синхронизация зависимостей с файлом [pyproject.toml](pyproject.toml);
- `uv lock` - заморозка зависимостей и создание файла `uv.lock`, который рекомендуется добавлять в репозиторий.

## Документация
Документация расположена в [docs/](docs/README.md).