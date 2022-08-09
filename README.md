# Тестовая реализация асинхронного API с использованием Python и FastAPI

## Как запустить 

Запуск

````
$ docker-compose up -d --build
````

и переходим по ссылке: http://127.0.0.1:8000/docs

## Как выбрать схему БД

В файле .env в строке DATABASE_TYPE указать:
- db для использования PostgreSQL
- local для использования репозитория в памяти.