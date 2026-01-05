# Docker

## Очистка неиспользуемых образов, контейнеров, томов, сетей и кэша сборки
```bash
docker system prune -a --volumes
```

## Создание сети
```bash
docker network create ${PROJECT__NAME}-network
```
