#!/bin/bash
set -euo pipefail

# Список файлов, в которых нужно заменить строку
FILES=(
    "docker/docker-compose.yml"
    "docker/docker-compose-ci.yml"
)

# Спрашиваем у пользователя старое название
echo -e "Enter old PROJECT__NAME (e.g. UNSET__PROJECT__NAME):"
read -r OLD_PROJECT_NAME

if [[ -z "$OLD_PROJECT_NAME" ]]; then
    echo "ERROR: Old project name cannot be empty."
    exit 1
fi

# Читаем новое имя проекта из config/.env
if [[ ! -f "config/.env" ]]; then
    echo "ERROR: config/.env not found"
    exit 1
fi

NEW_PROJECT_NAME=$(grep -E '^PROJECT__NAME=' config/.env | cut -d '=' -f2-)

if [[ -z "$NEW_PROJECT_NAME" ]]; then
    echo "ERROR: PROJECT__NAME not set in config/.env"
    exit 1
fi

# Проходим по каждому файлу и заменяем строку
for file in "${FILES[@]}"; do
    if [[ -f "$file" ]]; then
        sed -i "s/${OLD_PROJECT_NAME}/${NEW_PROJECT_NAME}/g" "$file"
        echo "Updated $file"
    else
        echo "WARNING: $file not found, skipping."
    fi
done

echo "All done!"