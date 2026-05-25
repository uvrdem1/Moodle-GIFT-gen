def build_generation_prompt(
    topic: str,
    questions_count: int,
    language: str,
    question_type: str,
    answers_count: int,
    source_text: str
) -> str:

    question_type_text = {
        "single": "single choice",
        "multiple": "multiple choice",
        "truefalse": "true/false"
    }.get(question_type, "single choice")


    prompt = f"""
Ты профессиональный методист Moodle и эксперт по созданию тестов.

Твоя задача:
сгенерировать РОВНО {questions_count} качественных вопросов в формате GIFT.

ВАЖНЕЙШИЕ ПРАВИЛА:

1. Сгенерируй РОВНО {questions_count} вопросов.
Нельзя генерировать больше.
Нельзя генерировать меньше.

2. НЕ ПИШИ:
- пояснения
- комментарии
- markdown
- ``` 
- текст вне GIFT

3. НЕ ПИШИ:
- "(пропущенный вопрос)"
- "вопрос 1"
- "конец теста"
- любые служебные фразы

4. Возвращай ТОЛЬКО чистый GIFT.

5. Каждый вопрос должен быть:
- уникальным
- понятным
- логичным
- без повторений

6. Язык вопросов: {language}

7. Тип вопросов: {question_type_text}

8. Количество вариантов ответа:
{answers_count}

9. Используй ТОЛЬКО информацию из материала.
Не придумывай факты вне текста.

10. Формат должен быть СТРОГО совместим с Moodle GIFT.

ПРИМЕР ПРАВИЛЬНОГО ФОРМАТА:

::Question 1::
Какой оператор используется для создания функции в Python?
{{
=def
~func
~function
~lambda
}}

::Question 2::
Как обозначается комментарий в Python?
{{
=# комментарий
~// комментарий
~/* комментарий */
~<!-- комментарий -->
}}

ТЕМА:
{topic}

МАТЕРИАЛ:
{source_text}

Сгенерируй РОВНО {questions_count} вопросов.
Верни ТОЛЬКО GIFT.
"""

    return prompt