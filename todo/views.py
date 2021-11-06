from rest_framework.viewsets import ModelViewSet   
from todo.models import Todo
from todo.serializers import TodoSerializer
class TodoViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()