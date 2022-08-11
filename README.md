# api_yamdb
api_yamdb

### Описание
Проект YaMDb собирает рейтинг и отзывы пользователей
на произведения, которые делятся на категории
(«Книги», «Фильмы», «Музыка») и жанры.

### Разработчики проекта
- [Бочкарёв Владислав (тимлид, разработка ресурсов Review и Comments)](https://github.com/somedAmn)
- [Рыбин Глеб (разработка ресурсов Categories, Genres и Titles)](https://github.com/BearLikesVodka)
- [Бланко Александра (разработка ресурсов Auth и Users)](https://github.com/AlexandraBlanko)

### Запуск приложения в контейнерах

1) Клонировать репозиторий и перейти в корневую папку:
```
git clone git@github.com:somedAmn/infra_sp2.git
cd infra_sp2
```

2) Перейти в папку infra_sp2/infra и создать в ней файл .env с 
переменными окружения, необходимыми для работы приложения.
```
cd infra/
```

Пример содержимого файла:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=key
```

3) Запустить docker-compose: 
```
docker-compose up -d
```

4) Выполнить миграции, создать суперпользователя и собрать статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```
5) Проект доступен по адресу http://localhost/

### Заполнение базы данных

Нужно зайти на на http://localhost/admin/, авторизоваться и внести записи 
в базу данных через админку.

Резервную копию базы данных можно создать командой
```
docker-compose exec web python manage.py dumpdata > fixtures.json 
```

### Остановка контейнеров

Для остановки работы приложения можно набрать в терминале команду Ctrl+C 
либо открыть второй терминал и воспользоваться командой
```
docker-compose stop 
```
Также можно запустить контейнеры без их создания заново командой
```
docker-compose start 
```
### Примеры запросов

Регистрация нового пользователя

POST:

```
http://127.0.0.1:8000/api/v1/auth/signup/
```

Получение JWT-токена

POST:

```
http://127.0.0.1:8000/api/v1/auth/token/
```

Получение пользователя по username

GET:

```
http://127.0.0.1:8000/api/v1/users/{username}/
```

Изменение данных своей учетной записи

PATCH

```
http://127.0.0.1:8000/api/v1/users/me/
```
