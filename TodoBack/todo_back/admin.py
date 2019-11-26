from django.contrib import admin
from todo_back.models import TodoList, TodoItem

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoList)
admin.site.register(TodoItem, TodoAdmin)
