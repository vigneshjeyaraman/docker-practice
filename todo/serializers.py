from rest_framework import serializers
from todo.models import Todo
from users.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Todo
        exclude = ("created_at", "updated_at")

class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("created_at", "updated_at", "created_by")
