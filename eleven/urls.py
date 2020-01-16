from django.urls import path
from .views      import ElevenRegister

urlpatterns = [
    path('/register', ElevenRegister.as_view()),
]