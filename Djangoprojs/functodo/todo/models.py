from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=200, blank=False, null=False)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo
