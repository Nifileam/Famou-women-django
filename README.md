[🇷🇺 Читать на русском](#russian)

---

<a name="english"></a>

# Famous Women Blog

A Django-based blog about famous women, featuring user authentication, Google OAuth, category and tag filtering, an admin panel, captcha protection, and XML sitemap support.

---

## Tech Stack

- **Python 3.13** / **Django 6.0**
- **PostgreSQL** — main database
- **Pillow** — image upload and processing
- **social-auth-app-django** — Google OAuth2 login
- **django-simple-captcha** — captcha on the contact form
- **django-debug-toolbar** — development profiling
- **python-decouple** — environment variable management
- **Django Sitemaps** — auto-generated XML sitemap

---

## Features

- 📰 **Posts** — create, edit, and view articles about famous women with photo upload
- 🗂 **Categories & Tags** — filter posts by category or tag
- 👤 **User authentication** — register, login, logout, password reset via email
- 🔐 **Google OAuth2** — sign in with a Google account
- ✏️ **Add & Edit posts** — only available to authenticated users; users can only edit their own posts
- 🛡 **Admin panel** — full content management via Django Admin
- 📋 **Contact form** — with captcha protection
- 🗺 **XML Sitemap** — for search engine indexing
- 🔒 **Custom authentication backend** — login via email in addition to username
- 🖼 **Default user avatar** — assigned automatically on registration

---

## Project Structure

```
project/
├── famouswomen/        # Main app (posts, categories, tags)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── sitemaps.py
│   └── templates/
├── users/              # Authentication app
│   ├── models.py
│   ├── views.py
│   ├── authentication.py
│   └── templates/
├── news/               # Django project settings
│   ├── settings.py
│   └── urls.py
├── media/              # Uploaded files (not tracked by git)
├── .env                # Environment variables (not tracked by git)
├── .env.example        # Example env file
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nifileam/Famou-women-django.git
cd famous-women-django
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
```

### 5. Create the database and apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Create the media directory

```bash
mkdir media
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `EMAIL_HOST_USER` | Gmail address for sending emails |
| `EMAIL_HOST_PASSWORD` | Gmail app password for sending emails |
| `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY` | Google OAuth2 client ID |
| `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET` | Google OAuth2 client secret |

---

## Author

Created as a pet project to practice Django development.

---
---

[🇬🇧 Read in English](#english)

<a name="russian"></a>

# Famous Women Blog

Блог на Django о знаменитых женщинах. Реализованы регистрация и авторизация пользователей, вход через Google, фильтрация по категориям и тегам, админ-панель, капча и XML-карта сайта.

---

## Стек технологий

- **Python 3.13** / **Django 6.0**
- **PostgreSQL** — основная база данных
- **Pillow** — загрузка и обработка изображений
- **social-auth-app-django** — авторизация через Google OAuth2
- **django-simple-captcha** — капча в форме обратной связи
- **django-debug-toolbar** — профилирование в режиме разработки
- **python-decouple** — управление переменными окружения
- **Django Sitemaps** — автоматическая генерация XML-карты сайта

---

## Функциональность

- 📰 **Статьи** — создание, редактирование и просмотр публикаций с загрузкой фото
- 🗂 **Категории и теги** — фильтрация публикаций
- 👤 **Аутентификация** — регистрация, вход, выход, сброс пароля по email
- 🔐 **Google OAuth2** — вход через аккаунт Google
- ✏️ **Добавление и редактирование статей** — только для авторизованных пользователей; пользователи могут редактировать только свои публикации
- 🛡 **Админ-панель** — полное управление контентом через Django Admin
- 📋 **Форма обратной связи** — с защитой капчей
- 🗺 **XML Sitemap** — для индексации поисковыми системами
- 🔒 **Кастомный backend аутентификации** — вход по email помимо username
- 🖼 **Аватар по умолчанию** — устанавливается автоматически при регистрации

---

## Структура проекта

```
project/
├── famouswomen/        # Основное приложение (статьи, категории, теги)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── sitemaps.py
│   └── templates/
├── users/              # Приложение аутентификации
│   ├── models.py
│   ├── views.py
│   ├── authentication.py
│   └── templates/
├── news/               # Настройки Django-проекта
│   ├── settings.py
│   └── urls.py
├── media/              # Загружаемые файлы (не отслеживается git)
├── .env                # Переменные окружения (не отслеживается git)
├── .env.example        # Пример env-файла
└── requirements.txt
```

---

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ваш-username/famous-women-django.git
cd famous-women-django
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения

Скопируйте `.env.example` в `.env` и заполните своими данными:

```bash
cp .env.example .env
```

```env
SECRET_KEY=ваш-секретный-ключ
DB_NAME=имя_базы_данных
DB_USER=пользователь_бд
DB_PASSWORD=пароль_бд
EMAIL_HOST_USER=ваш-gmail@gmail.com
EMAIL_HOST_PASSWORD=пароль-приложения-gmail
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=ваш-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=ваш-google-client-secret
```

### 5. Создать базу данных и применить миграции

```bash
python manage.py migrate
```

### 6. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 7. Создать папку media

```bash
mkdir media
```

### 8. Запустить сервер разработки

```bash
python manage.py runserver
```

Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере.

---

## Переменные окружения

| Переменная | Описание |
|---|---|
| `SECRET_KEY` | Секретный ключ Django |
| `DB_NAME` | Название базы данных PostgreSQL |
| `DB_USER` | Пользователь PostgreSQL |
| `DB_PASSWORD` | Пароль PostgreSQL |
| `EMAIL_HOST_USER` | Gmail адрес для отправки писем |
| `EMAIL_HOST_PASSWORD` | Пароль приложения Gmail для отправки писем |
| `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY` | Client ID Google OAuth2 |
| `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET` | Client Secret Google OAuth2 |

---

## Автор

Создано как pet-проект для практики разработки на Django.
