from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.gift_generator import (
    build_gift_questions
)

import traceback


@api_view(['POST'])
def generate_questions(request):

    try:
        data = request.data

        topic = data.get('topic')
        questions_count = data.get('questions_count')
        language = data.get('language')
        question_type = data.get('question_type')
        answers_count = data.get('answers_count')
        material = data.get('material')

        result = build_gift_questions(
            topic=topic,
            questions_count=questions_count,
            language=language,
            question_type=question_type,
            answers_count=answers_count,
            material=material
        )

        return Response({
            'result': result
        })

    except Exception as e:

        traceback.print_exc()

        return Response({
            'error': str(e)
        }, status=500)


@api_view(['GET'])
def test_api(request):

    return Response({
        'status': 'ok'
    })