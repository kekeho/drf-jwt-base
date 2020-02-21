from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from .views import UserRegister

urlpatterns = [
    path('jwt-token/', obtain_jwt_token),
    path('register/', UserRegister.as_view()),
]
