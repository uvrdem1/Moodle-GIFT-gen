# Moodle GIFT Generator

Веб-приложение для генерации тестовых вопросов в формате Moodle GIFT с использованием больших языковых моделей (LLM).

Рабочая версия: [http://81.26.187.243/](http://81.26.187.243/)

Проект разработан в рамках дипломной работы:

> «Фронтенд-разработка веб-приложения для генерации вопросов и ответов в формате GIFT для системы дистанционного обучения Moodle с использованием больших языковых моделей»

---

# Основные возможности

- AI-генерация тестовых вопросов
- Поддержка формата Moodle GIFT
- Выбор между GigaChat и ChatGPT
- Интеграция с GigaChat API и OpenAI Responses API
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
- OpenAI Responses API
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
AI Provider (GigaChat / ChatGPT)
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
│   ├── openai_client.py
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
│   └── index.css
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
- Выбор нейросети
- Генерацию по пользовательскому тексту
- Историю генераций
- Скачивание результатов
- Копирование результата
- Редактирование GIFT

---

# Установка проекта

## Требования

- Python 3.12 или новее
- Node.js 20.19 или новее
- npm

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
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
CSRF_TRUSTED_ORIGINS=
SQLITE_PATH=

GIGACHAT_AUTH_KEY=ваш_ключ_gigachat
GIGACHAT_VERIFY_SSL=True

OPENAI_API_KEY=ваш_ключ_openai
OPENAI_MODEL=gpt-5.5
```

Для работы достаточно настроить ключ выбранной нейросети. Использование OpenAI API требует отдельного API-аккаунта с доступной квотой; подписка ChatGPT не заменяет API-биллинг.

---

## Применение миграций

```bash
python manage.py migrate
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

Откройте второй терминал и перейдите из корня проекта в папку frontend:

```bash
cd frontend
```

---

## Установка зависимостей

```bash
npm install
```

---

## Настройка API

Создайте файл `frontend/.env` по примеру `.env.example`:

```text
VITE_API_URL=http://127.0.0.1:8000/api
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
- Формирования синтаксиса Moodle GIFT
- Формирования промптов по заданным параметрам
- Генерации различных типов вопросов
- Мультиязычной обработки текста

---

# Реализованные возможности

Во время разработки были реализованы:

- Модульная frontend архитектура
- Сервисная backend архитектура
- JWT система авторизации
- Интеграция с GigaChat API и OpenAI Responses API
- Выбор языковой модели
- Динамическое формирование промпта
- Поддержка Moodle GIFT
- Редактируемый результат генерации
- История генераций
- Экспорт `.gift`
- Современный UI интерфейс

---

# Возможные направления развития

- PostgreSQL
- Контейнеризация с Docker
- Подключение дополнительных языковых моделей
- Загрузка PDF/TXT файлов
- Интеграция с Moodle API
- RAG архитектура
- Автоматическая валидация вопросов
- Анализ качества тестов

---

# Назначение проекта

Проект разработан в учебных целях в рамках дипломной работы.

---

# Автор

Уваров Демьян Васильевич
