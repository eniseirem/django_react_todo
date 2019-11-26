from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(get_user_model(), null=True, default=1, on_delete=models.DO_NOTHING)

class TodoItem (models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    dependency = models.CharField(max_length=120, default=None)

    def clean(self):
        if self.dependency is not None:
            raise ValidationError(_('This item can not be deleted, depented on' + self.depent))
