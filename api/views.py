from rest_framework import generics

from todolist.models import ToDoList
from .serializers import ToDoListSerializer


class ToDoListAPIView(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
