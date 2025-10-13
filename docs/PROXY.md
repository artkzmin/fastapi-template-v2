# SOCKS5-прокси

## Установка `microsocks` на сервере
```bash
sudo apt update && sudo apt install -y build-essential git
git clone https://github.com/rofl0r/microsocks.git
cd microsocks
make
sudo cp microsocks /usr/local/bin/
```

## Запуск
### Запуск через systemd (с автозапуском при перезагрузке)

- Открыть файл
```bash
sudo vim /etc/systemd/system/microsocks.service
```

- Вставить конфигурацию:
```bash
[Unit]
Description=MicroSocks Proxy Server
After=network.target

[Service]
ExecStart=/usr/local/bin/microsocks -p 1080 -u vpnuser -P mypassword
Restart=always
User=nobody
StandardOutput=append:/var/log/microsocks.log
StandardError=append:/var/log/microsocks.err.log

[Install]
WantedBy=multi-user.target
```

- Перезапуск systemd:
```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable microsocks
sudo systemctl start microsocks
```

- Проверка статуса:
```bash
sudo systemctl status microsocks.service
```

### Обычный
- `vpnuser` - имя пользователя
- `mypassword` - пароль
```bash
sudo nohup microsocks -p 1080 -u vpnuser -P mypassword > /var/log/microsocks.log 2>&1 &
```

## Прокинуть порт

```bash
sudo ufw allow 1080/tcp
```

## Тест прокси
```bash
curl -x http://vpnuser:mypassword@proxy.host:1080 http://ifconfig.me
```