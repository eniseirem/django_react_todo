from rest_framework import serializers
from .models import TodoItem, TodoList

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'list', 'name', 'desc', 'status', 'creation', 'deadline', 'dependency')

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'owner')
