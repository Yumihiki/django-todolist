from django.urls import path
from .views import ToDoListAPIView


urlpatterns = [
  path('', ToDoListAPIView.as_view()),
]