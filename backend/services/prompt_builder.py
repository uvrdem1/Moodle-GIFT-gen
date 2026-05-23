from typing import Optional


def build_generation_prompt(
    topic: str,
    questions_count: int,
    language: str,
    question_type: str,
    answers_count: int,
    source_text: Optional[str] = ''
) -> str:

    language_name = (
        'Русский'
        if language == 'ru'
        else 'English'
    )

    rules = ''

    if question_type == 'single':

        rules = f'''
Каждый вопрос должен содержать только один правильный ответ.
Используй ровно {answers_count} вариантов ответа.
'''

    elif question_type == 'boolean':

        rules = '''
Создавай только TRUE/FALSE вопросы.
'''

    elif question_type == 'multiple':

        rules = f'''
Каждый вопрос должен содержать несколько правильных ответов.
Используй ровно {answers_count} вариантов ответа.
'''

    prompt = f"""
Создай {questions_count} тестовых вопросов.

ТЕМАТИКА:
{topic}

ЯЗЫК:
{language_name}

МАТЕРИАЛ:
{source_text}

ПРАВИЛА:
{rules}

ОБЩИЕ ТРЕБОВАНИЯ:
- Верни только Moodle GIFT format
- Без markdown
- Без комментариев
- Без пояснений
- Не добавляй техническую информацию
- Не используй слова single, multiple, boolean
- Не добавляй информацию о количестве правильных ответов
- Используй только предоставленный материал

ПРИМЕР:

::Вопрос 1::
Что такое Python?
{{
=Язык программирования
~База данных
~Браузер
~Операционная система
}}
"""

    return prompt