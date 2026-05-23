from django.urls import path

from .views import (
    test_api,
    generate_questions
)

urlpatterns = [
    path('test/', test_api),
    path('generate/', generate_questions),
]   