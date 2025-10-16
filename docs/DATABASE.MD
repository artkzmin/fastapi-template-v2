# База данных
## Основная БД
### Поднятие базы данных в Docker-контейнере

```bash
. config/.env
docker run -d \
  --name "${PROJECT__NAME}-psql" \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -e POSTGRES_USER=${DB__USER} \
  -e POSTGRES_PASSWORD=${DB__PASSWORD} \
  -e POSTGRES_DB=${DB__NAME} \
  -v ${PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB__PORT}:5432 \
  postgres:15
```

### Пересоздание базы данных

```bash
. config/.env
docker rm -f "${PROJECT__NAME}-psql"
docker volume rm "${PROJECT__NAME}-pgdata"

docker run -d \
  --name "${PROJECT__NAME}-psql" \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -e POSTGRES_USER=${DB__USER} \
  -e POSTGRES_PASSWORD=${DB__PASSWORD} \
  -e POSTGRES_DB=${DB__NAME} \
  -v ${PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB__PORT}:5432 \
  postgres:15
```

---

## Тестовая БД

### Поднятие базы данных в Docker-контейнере

```bash
. config/.test.env
docker run -d \
  --name "${PROJECT__NAME}-psql" \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -e POSTGRES_USER=${DB__USER} \
  -e POSTGRES_PASSWORD=${DB__PASSWORD} \
  -e POSTGRES_DB=${DB__NAME} \
  -v ${PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB__PORT}:5432 \
  postgres:15
```

### Пересоздание базы данных

```bash
. config/.test.env
docker rm -f "${PROJECT__NAME}-psql"
docker volume rm "${PROJECT__NAME}-pgdata"

docker run -d \
  --name "${PROJECT__NAME}-psql" \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -e POSTGRES_USER=${DB__USER} \
  -e POSTGRES_PASSWORD=${DB__PASSWORD} \
  -e POSTGRES_DB=${DB__NAME} \
  -v ${PROJECT__NAME}-pgdata:/var/lib/postgresql/data \
  -p ${DB__PORT}:5432 \
  postgres:15
```

---

## Redis
### Поднятие контейнера

```bash
. config/.env
docker run -d \
  --name redis-pass \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -p ${REDIS__PORT}:6379 \
  -e REDIS_PASSWORD=${REDIS__PASSWORD} \
  redis:7 \
  redis-server --requirepass ${REDIS__PASSWORD}
```

### Пересоздание контейнера

```bash
. config/.env
docker rm -f redis-pass

docker run -d \
  --name redis-pass \
  --restart unless-stopped \
  --network ${PROJECT__NAME}-network \
  -p ${REDIS__PORT}:6379 \
  -e REDIS_PASSWORD=${REDIS__PASSWORD} \
  redis:7 \
  redis-server --requirepass ${REDIS__PASSWORD}
```