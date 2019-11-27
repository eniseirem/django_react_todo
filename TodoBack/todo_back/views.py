from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoItemSerializer, TodoListSerializer
from .models import TodoItem, TodoList


class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()

class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()