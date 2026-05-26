from django.contrib.auth import authenticate

from rest_framework.decorators import (
    api_view,
    permission_classes
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer
from .models import GenerationHistory

from services.gift_generator import (
    build_gift_questions
)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    serializer = RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():

        user = serializer.save()

        refresh = RefreshToken.for_user(
            user
        )

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

    return Response(
        serializer.errors,
        status=400
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):

    username = request.data.get(
        'username'
    )

    password = request.data.get(
        'password'
    )

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:

        return Response(
            {
                'error': 'Invalid credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(
        user
    )

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_questions(request):

    topic = request.data.get(
        'topic'
    )

    questions_count = int(
        request.data.get(
            'questions_count',
            5
        )
    )

    language = request.data.get(
        'language',
        'ru'
    )

    question_type = request.data.get(
        'question_type',
        'single'
    )

    answers_count = int(
        request.data.get(
            'answers_count',
            4
        )
    )

    source_text = request.data.get(
        'source_text',
        ''
    )

    result = build_gift_questions(

        topic=topic,

        questions_count=questions_count,

        language=language,

        question_type=question_type,

        answers_count=answers_count,

        source_text=source_text
    )

    GenerationHistory.objects.create(

        user=request.user,

        topic=topic,

        question_type=question_type,

        questions_count=questions_count,

        answers_count=answers_count,

        language=language,

        source_text=source_text,

        result=result
    )

    return Response({
        'result': result
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):

    generations = GenerationHistory.objects.filter(
        user=request.user
    ).order_by('-created_at')

    data = []

    for item in generations:

        data.append({

            'id': item.id,

            'topic': item.topic,

            'question_type': item.question_type,

            'questions_count': item.questions_count,

            'answers_count': item.answers_count,

            'language': item.language,

            'source_text': item.source_text,

            'result': item.result,

            'created_at': item.created_at,
        })

    return Response(data)