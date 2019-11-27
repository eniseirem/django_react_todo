from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(get_user_model(), default=1, on_delete=models.DO_NOTHING)

class TodoItem (models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, db_column="name")
    desc = models.TextField()
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    dependency = models.ForeignKey("TodoItem", to_field="id", null=True, blank=True, default=None, on_delete=models.DO_NOTHING)


    # def todo_done(self):
    #     if self.dependency is not None:
    #         #check status of dependent item
    #         raise ValidationError(_('This item can not be deleted, depented on' + self.dependency))
    #     else:
    #         self.status = True
