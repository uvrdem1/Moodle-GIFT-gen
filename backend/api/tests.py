from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import GenerationHistory


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
