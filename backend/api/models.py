from django.db import models
from django.contrib.auth.models import User


class GenerationHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='generations'
    )

    topic = models.CharField(
        max_length=255
    )

    question_type = models.CharField(
        max_length=100
    )

    questions_count = models.IntegerField()

    answers_count = models.IntegerField()

    language = models.CharField(
        max_length=50
    )

    model_provider = models.CharField(
        max_length=50,
        default='gigachat'
    )

    source_text = models.TextField()

    result = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.topic
