from django.contrib import admin
from todo_back.models import TodoList, TodoItem

# Register your models here.
class TodoInline(admin.StackedInline):
    model = TodoItem
    fk_name = 'list'

class TodoAdmin(admin.ModelAdmin):
    inlines = [
                TodoInline,
               ]

admin.site.register(TodoList,TodoAdmin)
