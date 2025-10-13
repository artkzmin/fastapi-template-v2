# Docker

## Очистка неиспользуемых образов, контейнеров, томов, сетей и кэша сборки
```bash
docker system prune -a --volumes
```

## Создание сети для Docker контейнеров
```bash
. config/.env
docker network create ${CONFIG__PROJECT__NAME}-network
```