import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)

from dotenv import load_dotenv
from gigachat import GigaChat


load_dotenv()


def generate_gigachat_questions(
    topic,
    questions_count=5,
    language='ru',
    question_type='single',
    answers_count=4,
    source_text=''
):

    credentials = os.getenv(
        "GIGACHAT_CREDENTIALS"
    )

    if not credentials:
        raise Exception(
            "GIGACHAT_CREDENTIALS not found"
        )

    language_name = (
        'Русский'
        if language == 'ru'
        else 'English'
    )

    question_type_text = {
        'single': 'Один правильный ответ',
        'boolean': 'Верно / Неверно',
        'multiple': 'Множественный выбор'
    }.get(question_type)

    prompt = f"""
Создай {questions_count} вопросов.

ТЕМАТИКА:
{topic}

ЯЗЫК:
{language_name}

ТИП ВОПРОСА:
{question_type_text}

КОЛИЧЕСТВО ВАРИАНТОВ ОТВЕТА:
{answers_count}

ТЕКСТ:
{source_text}

ТРЕБОВАНИЯ:
- Верни ТОЛЬКО Moodle GIFT format
- Без markdown
- Без объяснений
- Без code blocks
- Используй только предоставленный текст
- Вопросы должны быть корректными

ЕСЛИ тип:
- single → один правильный ответ
- boolean → TRUE/FALSE
- multiple → несколько правильных ответов

Пример:

::Вопрос 1::
Что такое Python?
{{
=Язык программирования
~База данных
~Браузер
~Операционная система
}}
"""

    try:

        with GigaChat(
            credentials=credentials,
            verify_ssl_certs=False
        ) as giga:

            response = giga.chat(prompt)

            return response.choices[0].message.content

    except Exception as error:

        print(error)

        raise error