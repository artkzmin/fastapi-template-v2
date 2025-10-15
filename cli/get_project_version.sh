#!/bin/bash
# Скрипт получает версию проекта из pyproject.toml

set -euo pipefail

PYPROJECT_FILE="pyproject.toml"

if [[ ! -f "$PYPROJECT_FILE" ]]; then
  echo "Ошибка: файл $PYPROJECT_FILE не найден" >&2
  exit 1
fi

# Извлечение версии (работает для большинства форматов Poetry)
version=$(grep -E '^version\s*=' "$PYPROJECT_FILE" | head -n 1 | sed -E 's/.*=\s*"([^"]+)".*/\1/')

if [[ -z "$version" ]]; then
  echo "Ошибка: не удалось найти версию в $PYPROJECT_FILE" >&2
  exit 1
fi

echo "$version"