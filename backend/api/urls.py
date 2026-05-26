from django.urls import path

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

        'generate/',

        generate_questions
    ),

    path(

        'history/',

        history
    ),
]