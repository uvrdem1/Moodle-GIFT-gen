from services.prompt_builder import (
    build_generation_prompt
)

from services.gigachat_client import (
    request_gigachat
)


def build_gift_questions(
    topic: str,
    questions_count: int,
    language: str,
    question_type: str,
    answers_count: int,
    source_text: str
) -> str:

    prompt = build_generation_prompt(
        topic=topic,
        questions_count=questions_count,
        language=language,
        question_type=question_type,
        answers_count=answers_count,
        source_text=source_text
    )

    result = request_gigachat(
        prompt
    )

    return result