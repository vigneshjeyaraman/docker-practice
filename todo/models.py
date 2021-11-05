from django.db import models

# Create your models here.
from users.models import User

class Todo(models.Model):
    """
        Todo model to hold todo data
    """
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    end_data = models.DateField()
    created_by = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    STATUS = (
        (1, "open"),
        (0, "close")
    )
    status = models.CharField(choices=STATUS, max_length=5)