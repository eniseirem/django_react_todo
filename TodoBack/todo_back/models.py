from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(get_user_model(), default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.title)

class TodoItem (models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, db_column="name")
    desc = models.TextField()
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    dependency = models.ForeignKey("TodoItem", to_field="id", null=True, blank=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
