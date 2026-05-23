# AI Moodle GIFT Generator

Веб-приложение для генерации тестовых вопросов в формате Moodle GIFT с использованием больших языковых моделей (LLM).

---

# Возможности

- Генерация тестовых вопросов через AI
- Поддержка Moodle GIFT format
- Поддержка GigaChat
- Выбор языка генерации
- Выбор типа вопроса
- Генерация по пользовательскому тексту
- Редактирование результата
- Экспорт `.gift`
- Современный AI интерфейс

---

# Используемые технологии

## Frontend

- React
- TypeScript
- Vite
- TailwindCSS
- Framer Motion
- Axios
- Lucide React

## Backend

- Django
- Django REST Framework
- Python
- GigaChat API
- Python Dotenv
- Django CORS Headers

---

# Архитектура проекта

```text
React Frontend
↓
Django REST API
↓
GigaChat Service
↓
Moodle GIFT Generator
```

---

# Поддерживаемые типы вопросов

- Один правильный ответ
- Верно / Неверно
- Множественный выбор

---

# Структура проекта

```text
backend/
│
├── api/
├── services/
├── backend/
├── manage.py
│
frontend/
│
├── src/
├── public/
├── package.json
└── vite.config.ts
```

---

# Установка проекта

## 1. Клонирование репозитория

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

## Активация виртуального окружения

### Windows

```bash
.\venv\Scripts\activate
```

---

## Установка зависимостей

```bash
pip install django djangorestframework python-dotenv gigachat django-cors-headers
```

---

## Настройка .env

Создайте файл:

```text
.env
```

### Добавьте:

```env
GIGACHAT_CREDENTIALS=YOUR_GIGACHAT_CREDENTIALS
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

# Интерфейс приложения

Приложение поддерживает:

- Выбор нейросети
- Выбор языка генерации
- Тип вопросов
- Количество вопросов
- Количество вариантов ответа
- Тематику вопросов
- Генерацию по пользовательскому тексту
- Редактирование результата
- Копирование результата
- Экспорт `.gift`

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
- Генерации Moodle GIFT syntax
- Анализа пользовательского текста
- Создания различных типов вопросов
- Мультиязычной генерации

---

# Используемые AI технологии

- Prompt Engineering
- REST API Integration
- Dynamic Question Generation
- Moodle GIFT Formatting
- LLM-based Text Processing

---

# Планы по развитию

- Поддержка ChatGPT API
- Авторизация пользователей
- История генераций
- Загрузка PDF/TXT файлов
- PostgreSQL
- Docker
- Moodle API Integration
- AI Quality Validation
- RAG Integration

---

# Автор

Demian Uvarov

---

# Лицензия

MIT