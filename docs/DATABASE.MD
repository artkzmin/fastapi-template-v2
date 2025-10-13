# БД

## Основная БД
Поднятие БД в Docker-контейнере:
```bash
. config/.env
docker run -d \
  --name "${CONFIG__PROJECT__NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${CONFIG__DB__USER} \
  -e POSTGRES_PASSWORD=${CONFIG__DB__PASSWORD} \
  -e POSTGRES_DB=${CONFIG__DB__NAME} \
  -v ${CONFIG__PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${CONFIG__DB__PORT}:5432 \
  postgres:15
```

Пересоздание БД:
```bash
. config/.env
docker rm -f "${CONFIG__PROJECT__NAME}-psql"
docker volume rm "${CONFIG__PROJECT__NAME}-pgdata"
docker run -d \
  --name "${CONFIG__PROJECT__NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${CONFIG__DB__USER} \
  -e POSTGRES_PASSWORD=${CONFIG__DB__PASSWORD} \
  -e POSTGRES_DB=${CONFIG__DB__NAME} \
  -v ${CONFIG__PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${CONFIG__DB__PORT}:5432 \
  postgres:15
```

## Тестовая БД
Поднятие БД в Docker-контейнере:
```bash
. config/.test.env
docker run -d \
  --name "${CONFIG__PROJECT__NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${CONFIG__DB__USER} \
  -e POSTGRES_PASSWORD=${CONFIG__DB__PASSWORD} \
  -e POSTGRES_DB=${CONFIG__DB__NAME} \
  -v ${CONFIG__PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${CONFIG__DB__PORT}:5432 \
  postgres:15
```

Пересоздание БД:
```bash
. config/.test.env
docker rm -f "${CONFIG__PROJECT__NAME}-psql"
docker volume rm "${CONFIG__PROJECT__NAME}-pgdata"
docker run -d \
  --name "${CONFIG__PROJECT__NAME}-psql" \
  --restart unless-stopped \
  -e POSTGRES_USER=${CONFIG__DB__USER} \
  -e POSTGRES_PASSWORD=${CONFIG__DB__PASSWORD} \
  -e POSTGRES_DB=${CONFIG__DB__NAME} \
  -v ${CONFIG__PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${CONFIG__DB__PORT}:5432 \
  postgres:15
```