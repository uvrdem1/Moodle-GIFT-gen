from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.gift_generator import (
    build_gift_questions
)


@api_view(['GET'])
def test_api(request):

    return Response({
        'message': 'API works!'
    })


@api_view(['POST'])
def generate_questions(request):

    try:

        topic: str = request.data.get(
            'topic',
            ''
        ).strip()

        questions_count: int = int(
            request.data.get(
                'questions_count',
                5
            )
        )

        language: str = request.data.get(
            'language',
            'ru'
        )

        question_type: str = request.data.get(
            'question_type',
            'single'
        )

        answers_count: int = int(
            request.data.get(
                'answers_count',
                4
            )
        )

        source_text: str = request.data.get(
            'source_text',
            ''
        ).strip()


        if not topic:

            return Response(
                {
                    'error': 'Topic is required'
                },
                status=400
            )


        result = build_gift_questions(
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


    except Exception as error:

        return Response(
            {
                'error': str(error)
            },
            status=500
        )