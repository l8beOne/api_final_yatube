# api_final_yatube
<h1 align="center"><img src="https://camo.githubusercontent.com/4fa9a5bdefafee7e59ad2086429306dfc0c902d0db4d2d1fdfb534b1767d9f62/68747470733a2f2f646576656c6f706572732e67697068792e636f6d2f6272616e63682f6d61737465722f7374617469632f6170692d35313264333663303936363236383237313731303861333862626235633537642e676966" height="300" width="400"/></h1>

## Описание проекта:
REST API для проекта Yatube. Реализована аутентификация по JWT токену. API (от англ. Application Programming Interface, «программный интерфейс приложения») — это интерфейс для обмена данными. Слово «программный» означает, что API служат в первую очередь для взаимодействия программ.
## Технологии:
* Python 3.9.10
* Django 3.2
* Django Rest Framework 3.12.4
* SQlite3
* Simple JWT
## Как запустить проект:
Склонируйте репозиторий:

```
git clone git@github.com:l8beOne/api_final_yatube.git
```

Установите и активируйте виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейдите в папку api_yamdb/api_yamdb и примените миграции.

```
python manage.py migrate
```

Запустите проект:

```
python manage.py runserver
```
