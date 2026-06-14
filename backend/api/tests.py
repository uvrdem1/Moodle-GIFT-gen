from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import GenerationHistory
from services.gift_generator import (
    build_gift_questions
)


class AuthTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_register_returns_tokens(self):
        response = self.client.post(
            '/api/register/',
            {
                'username': 'student',
                'password': 'strong-password-123'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class GenerationTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='student',
            password='strong-password-123'
        )
        self.client.force_authenticate(
            user=self.user
        )

    @patch('api.views.build_gift_questions')
    def test_generate_saves_history(self, build_gift_questions):
        build_gift_questions.return_value = (
            '::Question 1::\n'
            'Python is a programming language.{TRUE}'
        )

        response = self.client.post(
            '/api/generate/',
            {
                'topic': 'Python',
                'questions_count': 1,
                'question_type': 'truefalse',
                'answers_count': 2,
                'language': 'en',
                'source_text': 'Python is a programming language.'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            GenerationHistory.objects.count(),
            1
        )

    def test_generate_requires_topic(self):
        response = self.client.post(
            '/api/generate/',
            {
                'topic': '',
                'questions_count': 1
            },
            format='json'
        )

        self.assertEqual(response.status_code, 400)


class GiftGeneratorTests(TestCase):

    @patch('services.gift_generator.request_gigachat')
    def test_trims_extra_answers(self, request_gigachat):
        request_gigachat.return_value = (
            '::Question 1::\n'
            'First?\n'
            '{\n'
            '=One\n'
            '~Two\n'
            '~Three\n'
            '~Four\n'
            '}'
        )

        result = build_gift_questions(
            topic='Python',
            questions_count=1,
            language='en',
            question_type='single',
            answers_count=2,
            source_text=''
        )

        self.assertEqual(
            request_gigachat.call_count,
            1
        )
        self.assertIn(
            '=One\n~Two',
            result
        )
        self.assertNotIn(
            '~Three',
            result
        )

    @patch('services.gift_generator.request_gigachat')
    def test_retries_when_answer_count_is_too_low(self, request_gigachat):
        request_gigachat.side_effect = [
            (
                '::Question 1::\n'
                'First?\n'
                '{\n'
                '=One\n'
                '~Two\n'
                '}\n\n'
                '::Question 2::\n'
                'Second?\n'
                '{\n'
                '=One\n'
                '~Two\n'
                '}'
            ),
            (
                '::Question 1::\n'
                'First?\n'
                '{\n'
                '=One\n'
                '~Two\n'
                '~Three\n'
                '}\n\n'
                '::Question 2::\n'
                'Second?\n'
                '{\n'
                '=One\n'
                '~Two\n'
                '~Three\n'
                '}'
            )
        ]

        result = build_gift_questions(
            topic='Python',
            questions_count=2,
            language='en',
            question_type='single',
            answers_count=3,
            source_text=''
        )

        self.assertEqual(
            request_gigachat.call_count,
            2
        )
        self.assertIn(
            '::Question 2::',
            result
        )

    @patch('services.gift_generator.request_gigachat')
    def test_raises_when_fixed_answer_count_is_still_wrong(self, request_gigachat):
        request_gigachat.return_value = (
            '::Question 1::\n'
            'First?\n'
            '{\n'
            '=One\n'
            '~Two\n'
            '}'
        )

        with self.assertRaises(ValueError):
            build_gift_questions(
                topic='Python',
                questions_count=1,
                language='en',
                question_type='single',
                answers_count=3,
                source_text=''
            )
