# GitLab CI

## Установка GitLab Runner

```bash
docker run -d --name gitlab-runner --restart always \
  --dns 8.8.8.8 --dns 8.8.4.4 \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:alpine-v17.3.1
```

## Регистрация GitLab Runner внутри Docker

```bash
docker run --rm -it \
  --dns 8.8.8.8 --dns 8.8.4.4 \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  gitlab/gitlab-runner:alpine-v17.3.1 register
```

* Выберите executor — `docker`.
* Укажите default Docker image — `docker:dind`.

---

## Редактирование конфига

Откройте конфигурационный файл Runner'а:

```bash
sudo vim /srv/gitlab-runner/config/config.toml
```

Замените значение `volumes = ["/cache"]` на путь к проекту, указанному в переменной окружения `PROJECT__NAME` из директории [`config`](../config):

```bash
volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache", "/var/log/PROJECT__NAME/:/var/log/clear-talk/"]
```

---

## Переменные окружения

В разделе **CI/CD → Variables** в настройках GitLab проекта необходимо задать следующие переменные:

* **`ENV`** — файл, содержимое аналогично [`config/.env.dist`](../config/.env.dist);
* **`PROJECT__NAME`** — строковая переменная с названием проекта.
