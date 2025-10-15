# Gitlab CI

## Установка Gitlab Runner
```bash
docker run -d --name gitlab-runner --restart always \
  --dns 8.8.8.8 --dns 8.8.4.4 \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:alpine-v17.3.1
```

## Регистрация Gitlab Runner внутри Docker
```bash
docker run --rm -it \
  --dns 8.8.8.8 --dns 8.8.4.4 \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  gitlab/gitlab-runner:alpine-v17.3.1 register
```
- Выбрать executor - `docker`
- Выбрать default Docker image - `docker:dind`

## Редактирование конфига
```bash
sudo vim /srv/gitlab-runner/config/config.toml
```
Изменяем `volumes = ["/cache"]` на(заменить `PROJECT.NAME` на название проекта
из файла с переменными окружения в директории [config](../config)):
```bash
volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache", "/var/log/PROJECT.NAME/:/var/log/clear-talk/"]
```

## Переменные окружения
Через CI/CD variables в Gitlab нужно задать переменные окружения:
- `ENV` - как файл, содержимое аналогично [файлу](../config/.env.dist);
- `PROJECT.NAME` - обычная переменная, название проекта.