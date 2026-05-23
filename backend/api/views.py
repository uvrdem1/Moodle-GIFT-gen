from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.gigachat_service import (
    generate_gigachat_questions
)


@api_view(['GET'])
def test_api(request):

    return Response({
        'message': 'API works!'
    })


@api_view(['POST'])
def generate_questions(request):

    topic = request.data.get('topic')

    questions_count = request.data.get(
        'questions_count',
        5
    )

    provider = request.data.get(
        'provider',
        'gigachat'
    )

    language = request.data.get(
        'language',
        'ru'
    )

    question_type = request.data.get(
        'question_type',
        'single'
    )

    answers_count = request.data.get(
        'answers_count',
        4
    )

    source_text = request.data.get(
        'source_text',
        ''
    )

    result = generate_gigachat_questions(
        topic=topic,
        questions_count=questions_count,
        language=language,
        question_type=question_type,
        answers_count=answers_count,
        source_text=source_text
    )

    return Response({
        'gift': result
    })