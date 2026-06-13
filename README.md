# AI Moodle GIFT Generator

Веб-приложение для генерации тестовых вопросов в формате Moodle GIFT с использованием больших языковых моделей (LLM).

Проект разработан в рамках дипломной работы:

> «Фронтенд-разработка веб-приложения для генерации вопросов и ответов в формате GIFT для системы дистанционного обучения Moodle с использованием больших языковых моделей»

---

# Основные возможности

- AI-генерация тестовых вопросов
- Поддержка Moodle GIFT Format
- Интеграция с GigaChat API
- JWT авторизация
- История генераций
- Скачивание `.gift` файлов
- Поддержка нескольких типов вопросов
- Мультиязычная генерация
- Генерация по пользовательскому тексту
- Редактируемый результат генерации
- REST API архитектура
- Современный адаптивный интерфейс

---

# Поддерживаемые типы вопросов

- Один правильный ответ
- Множественный выбор
- Верно / Неверно

---

# Используемые технологии

## Frontend

- React
- TypeScript
- Vite
- TailwindCSS
- Axios
- React Router
- Framer Motion
- Lucide React

---

## Backend

- Django
- Django REST Framework
- JWT Authentication
- SQLite
- GigaChat API
- Python Dotenv
- Django CORS Headers

---

# Архитектура проекта

```text
React Frontend
      ↓
REST API
      ↓
Django Backend
      ↓
Prompt Builder
      ↓
GigaChat Client
      ↓
Moodle GIFT Generator
```

---

# Структура проекта

```text
backend/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── services/
│   ├── gigachat_client.py
│   ├── gift_generator.py
│   └── prompt_builder.py
│
├── backend/
│
├── manage.py
└── requirements.txt


frontend/
│
├── src/
│   ├── components/
│   │   ├── GeneratorForm.tsx
│   │   ├── Header.tsx
│   │   └── QuestionsPreview.tsx
│   │
│   ├── pages/
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   └── History.tsx
│   │
│   ├── api.ts
│   ├── App.jsx
│   ├── main.jsx
│   └── App.css
│
├── package.json
└── vite.config.ts
```

---

# Авторизация

Приложение использует JWT авторизацию:

- Регистрация пользователей
- Авторизация пользователей
- Access Token
- Refresh Token
- Защищённые API маршруты

---

# Основной функционал

Приложение поддерживает:

- Выбор тематики вопросов
- Выбор типа вопросов
- Количество вопросов
- Количество вариантов ответа
- Выбор языка генерации
- Генерацию по пользовательскому тексту
- Историю генераций
- Скачивание результатов
- Копирование результата
- Редактирование GIFT

---

# Установка проекта

## Клонирование репозитория

```bash
git clone https://github.com/uvrdem1/Moodle-GIFT-gen.git
```

---

# Backend запуск

## Переход в backend

```bash
cd backend
```

---

## Создание виртуального окружения

```bash
python -m venv venv
```

---

## Активация окружения

### Windows

```bash
.\venv\Scripts\activate
```

### MacOS / Linux

```bash
source venv/bin/activate
```

---

## Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Настройка переменных окружения

В папке `backend` создайте файл `.env` по примеру `.env.example`:

```text
DJANGO_SECRET_KEY=replace-me
DJANGO_DEBUG=True
GIGACHAT_AUTH_KEY=ваш_ключ_gigachat
```

---

## Запуск backend

```bash
python manage.py runserver
```

Backend будет доступен:

```text
http://127.0.0.1:8000
```

---

# Frontend запуск

## Переход в frontend

```bash
cd frontend
```

---

## Установка зависимостей

```bash
npm install
```

---

## Запуск frontend

```bash
npm run dev
```

Frontend будет доступен:

```text
http://localhost:5173
```

---

# Деплой

Один из простых вариантов деплоя:

- Backend: Render
- Frontend: Vercel

## Backend на Render

В проект добавлены файлы:

- `render.yaml`
- `backend/build.sh`
- `backend/Procfile`

На Render нужно создать Web Service из GitHub-репозитория и указать переменные окружения:

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=любой_длинный_секрет
DJANGO_ALLOWED_HOSTS=ваш-backend.onrender.com
CORS_ALLOWED_ORIGINS=https://ваш-frontend.vercel.app
CSRF_TRUSTED_ORIGINS=https://ваш-backend.onrender.com
GIGACHAT_AUTH_KEY=ваш_ключ_gigachat
GIGACHAT_VERIFY_SSL=False
```

После первого деплоя нужно скопировать адрес backend и добавить его в настройки frontend.

## Frontend на Vercel

Для Vercel:

- Root Directory: `frontend`
- Build Command: `npm run build`
- Output Directory: `dist`

Переменная окружения:

```text
VITE_API_URL=https://ваш-backend.onrender.com/api
```

После деплоя frontend нужно вернуться в Render и обновить:

```text
CORS_ALLOWED_ORIGINS=https://ваш-frontend.vercel.app
```

---

# Пример Moodle GIFT

## Один правильный ответ

```gift
::Вопрос 1::
Что такое Python?
{
=Язык программирования
~База данных
~Операционная система
~Браузер
}
```

---

## Множественный выбор

```gift
::Вопрос 2::
Какие технологии относятся к frontend?
{
=HTML
=CSS
~PostgreSQL
~Django
}
```

---

## Верно / Неверно

```gift
::Вопрос 3::
Python является языком программирования.
{
TRUE
}
```

---

# AI возможности

Приложение использует большие языковые модели для:

- Генерации тестов
- Формирования Moodle GIFT syntax
- Prompt Engineering
- Генерации различных типов вопросов
- Мультиязычной обработки текста

---

# Реализованные возможности

Во время разработки были реализованы:

- Модульная frontend архитектура
- Сервисная backend архитектура
- JWT система авторизации
- Интеграция с GigaChat API
- Динамическая генерация prompt
- Поддержка Moodle GIFT
- Редактируемый AI output
- История генераций
- Экспорт `.gift`
- Современный UI интерфейс

---

# Возможные направления развития

- PostgreSQL
- Docker deployment
- ChatGPT API integration
- Загрузка PDF/TXT файлов
- Moodle API Integration
- RAG архитектура
- AI валидация вопросов
- Анализ качества тестов

---

# Назначение проекта

Проект разработан в учебных целях в рамках дипломной работы.

---

# Автор

Demian Uvarov
