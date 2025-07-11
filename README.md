<h2>🚀 Установка и запуск</h2>


<h4>
1. Создайте файл .env в корневой директории 
</h4>

```requirements
PROJECT_NAME=
DEEPAI_API_KEY=
```

<h4>
2. Запустите docker compose:
</h4>

```commandline
docker compose up --build -d
```
Для запуска тестов можно использовать `curl`-запрос:
```bash
curl -X POST -F "file=@test.jpg" http://localhost/api/v1/moderate