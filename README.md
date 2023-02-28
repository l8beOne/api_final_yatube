# api_final

## Описание:

___

API (от англ. Application Programming Interface, «программный интерфейс приложения») — это интерфейс для обмена данными. Слово «программный» означает, что API служат в первую очередь для взаимодействия программ. 

___

## Установка

___

Установить виртуальное окружение, установить requirements.txt, запустить миграции

___

### Примеры

___

POST request на создание нового поста http://127.0.0.1:8000/api/v1/posts/:
{
    "text": "string",
    "image": "string",
    "group": 0
}
resonse:
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
