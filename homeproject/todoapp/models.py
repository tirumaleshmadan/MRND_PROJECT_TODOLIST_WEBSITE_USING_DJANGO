from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    name=models.CharField(max_length=128)
    created_date=models.DateTimeField()

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    description=models.CharField(max_length=256)
    due_date=models.DateField(null=True,blank=True)
    completed=models.BooleanField(default=False)

    list=models.ForeignKey(TodoList,on_delete=models.CASCADE)

    def __str__(self):
        return self.description