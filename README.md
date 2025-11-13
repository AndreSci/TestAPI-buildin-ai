# TestAPI-buildin.ai DJANGO + ORM

<img src="main_image.JPG" alt="Описание изображения" width="600">

[![Build Status](https://img.shields.io/badge/Python-3.12-green)](https://www.python.org/downloads/) ![Build Status](https://img.shields.io/badge/Docker-2025-blue) ![Build Status](https://img.shields.io/badge/PostgresSQL-2025-orange) ![Build Status](https://img.shields.io/badge/PyCharm-2025-green) ![Build Status](https://img.shields.io/badge/Django-2025-red)

## Описание

**TestAPI-buildin.ai** — это Python-приложение, тестовое написано с использованием Django и Postgres:

1. Регистрация событий.
2. Получения событий по статусу.
3. Обновления статуса события по id.

## Установка

1. **Клонирование репозитория:**

    ```bash
   git clone https://github.com/AndreSci/TestAPI-buildin-ai.git

2. **Установка через docker:**
    ```bash
   docker-compose up -d --build

---
### ЗАПУСТ ПРОИСХОДИТ АВТОМАТИЧЕСКИЙ В DOCKER 
Для запуска без Docker требуется ручное создание PostgresSQL базы данных с параметрами из .env файла.
Запуск Django проекта происходит из терминала - python manage.py runserver 
   
## Инструкция запросов

1. Создать инцидент
    ```bash
    POST - 127.0.0.1:8000/incidents/create/
   ```
    в боди запроса должен быть JSON
    ```
   {
    "msg": "some text",
    "status": "open",
    "source": "operator 404"
    }
   ```
---
2. Получить инциденты по статусу
    ```bash
   GET - 127.0.0.1:8000/incidents/?status=closed
   ```
   На данный момент свободный текст, но подразумевается что будут варианты "open\closed\progress"
    ```
    Params (заменить часть кода запроса): ?status=open
    ```
---
3. Обновить статус инцидента по ID
    ```bash
   POST or PUT - 127.0.0.1:8000/incidents/update_status/
   ```
   в body запроса должен быть JSON
   ```
   {
    "id": 1,
    "new_status": "closed"
   }
   ```