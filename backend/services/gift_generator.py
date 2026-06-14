import re

from services.prompt_builder import (
    build_generation_prompt
)

from services.gigachat_client import (
    request_gigachat
)


def _extract_answer_blocks(gift_text: str) -> list[str]:
    return re.findall(
        r'\{([^{}]*)\}',
        gift_text,
        flags=re.DOTALL
    )


def _count_answers(block: str) -> int:
    count = 0

    for line in block.splitlines():
        value = line.strip()

        if not value:
            continue

        if value.startswith(('=', '~')):
            count += 1
            continue

        if re.match(r'^%[-+]?\d+(\.\d+)?%', value):
            count += 1

    if count:
        return count

    return len(
        re.findall(
            r'(?<!\\)(=|~|%[-+]?\d+(\.\d+)?%)',
            block
        )
    )


def _find_answer_count_errors(
    gift_text: str,
    expected_count: int
) -> list[str]:
    blocks = _extract_answer_blocks(
        gift_text
    )

    errors = []

    for index, block in enumerate(
        blocks,
        start=1
    ):
        normalized = block.strip().upper()

        if normalized in ('TRUE', 'FALSE', 'T', 'F'):
            continue

        count = _count_answers(
            block
        )

        if count != expected_count:
            errors.append(
                f'question {index}: {count} answers'
            )

    return errors


def _is_answer_line(line: str) -> bool:
    value = line.strip()

    return (
        value.startswith(('=', '~')) or
        re.match(r'^%[-+]?\d+(\.\d+)?%', value) is not None
    )


def _normalize_answer_block(
    block: str,
    expected_count: int,
    question_type: str
) -> str:
    normalized = block.strip().upper()

    if normalized in ('TRUE', 'FALSE', 'T', 'F'):
        return block

    lines = [
        line.strip()
        for line in block.splitlines()
        if line.strip()
    ]

    answer_lines = [
        line
        for line in lines
        if _is_answer_line(line)
    ]

    if len(answer_lines) <= expected_count:
        return block

    correct_answers = [
        line
        for line in answer_lines
        if line.startswith('=') or line.startswith('%')
    ]

    wrong_answers = [
        line
        for line in answer_lines
        if line.startswith('~')
    ]

    if question_type == 'single' and correct_answers:
        selected = [
            correct_answers[0]
        ]
        selected.extend(
            wrong_answers[
                :expected_count - 1
            ]
        )
    else:
        selected = answer_lines[
            :expected_count
        ]

    if len(selected) != expected_count:
        return block

    return '\n' + '\n'.join(selected) + '\n'


def _normalize_answer_counts(
    gift_text: str,
    expected_count: int,
    question_type: str
) -> str:
    def replace_block(match):
        block = match.group(1)

        normalized = _normalize_answer_block(
            block=block,
            expected_count=expected_count,
            question_type=question_type
        )

        return '{' + normalized + '}'

    return re.sub(
        r'\{([^{}]*)\}',
        replace_block,
        gift_text,
        flags=re.DOTALL
    )


def _build_fix_prompt(
    gift_text: str,
    questions_count: int,
    question_type: str,
    answers_count: int
) -> str:
    return f"""
Исправь GIFT-текст ниже.

Правила:
- верни ТОЛЬКО чистый GIFT
- вопросов должно быть РОВНО {questions_count}
- тип вопросов: {question_type}
- в КАЖДОМ вопросе должно быть РОВНО {answers_count} вариантов ответа
- нельзя добавлять markdown, пояснения или комментарии

Текущий GIFT:
{gift_text}
"""


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

    if question_type != 'truefalse':
        result = _normalize_answer_counts(
            gift_text=result,
            expected_count=answers_count,
            question_type=question_type
        )

        errors = _find_answer_count_errors(
            result,
            answers_count
        )

        if errors:
            result = request_gigachat(
                _build_fix_prompt(
                    gift_text=result,
                    questions_count=questions_count,
                    question_type=question_type,
                    answers_count=answers_count
                )
            )

            result = _normalize_answer_counts(
                gift_text=result,
                expected_count=answers_count,
                question_type=question_type
            )

            errors = _find_answer_count_errors(
                result,
                answers_count
            )

            if errors:
                raise ValueError(
                    'Generated result has wrong answer count: '
                    + ', '.join(errors)
                )

    return result
