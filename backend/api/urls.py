from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (

    register,

    login_user,

    generate_questions,

    history,
)

urlpatterns = [

    path(

        'register/',

        register
    ),

    path(

        'login/',

        login_user
    ),

    path(

        'token/refresh/',

        TokenRefreshView.as_view()
    ),

    path(

        'generate/',

        generate_questions
    ),

    path(

        'history/',

        history
    ),
]
