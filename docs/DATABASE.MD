# БД

## Основная БД
Поднятие БД в Docker-контейнере:
```bash
. config/.env
docker run -d \
  --name "${PROJECT.NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${DB.USER} \
  -e POSTGRES_PASSWORD=${DB.PASSWORD} \
  -e POSTGRES_DB=${DB.NAME} \
  -v ${PROJECT.NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB.PORT}:5432 \
  postgres:15
```

Пересоздание БД:
```bash
. config/.env
docker rm -f "${PROJECT.NAME}-psql"
docker volume rm "${PROJECT.NAME}-pgdata"
docker run -d \
  --name "${PROJECT.NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${DB.USER} \
  -e POSTGRES_PASSWORD=${DB.PASSWORD} \
  -e POSTGRES_DB=${DB.NAME} \
  -v ${PROJECT.NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB.PORT}:5432 \
  postgres:15
```

## Тестовая БД
Поднятие БД в Docker-контейнере:
```bash
. config/.test.env
docker run -d \
  --name "${PROJECT.NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${DB.USER} \
  -e POSTGRES_PASSWORD=${DB.PASSWORD} \
  -e POSTGRES_DB=${DB.NAME} \
  -v ${PROJECT.NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB.PORT}:5432 \
  postgres:15
```

Пересоздание БД:
```bash
. config/.test.env
docker rm -f "${PROJECT.NAME}-psql"
docker volume rm "${PROJECT.NAME}-pgdata"
docker run -d \
  --name "${PROJECT.NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${DB.USER} \
  -e POSTGRES_PASSWORD=${DB.PASSWORD} \
  -e POSTGRES_DB=${DB.NAME} \
  -v ${PROJECT.NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB.PORT}:5432 \
  postgres:15
```