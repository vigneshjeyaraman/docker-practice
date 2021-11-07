from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("created_at", "updated_at")

class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("created_at", "updated_at", "created_by")
