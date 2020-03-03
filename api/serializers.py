from rest_framework import serializers

from todolist.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['author', 'title', 'content', 'status', 'updated_date']
    