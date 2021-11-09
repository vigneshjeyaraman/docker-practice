from rest_framework.viewsets import ModelViewSet   
from todo.models import Todo
from todo.serializers import TodoSerializer, CreateTodoSerializer
from rest_framework.permissions import IsAuthenticated
class TodoViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_class = (IsAuthenticated,)
    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user).all()
    
    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CreateTodoSerializer
        return TodoSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        