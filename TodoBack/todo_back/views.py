from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoItemSerializer, TodoListSerializer
from .models import TodoItem, TodoList
from rest_framework.decorators import action
from django.http import JsonResponse


class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()

    @action(methods=['get'], detail=True)
    def done(self, *args, **kwargs):
        todo = TodoItem.objects.get(id=kwargs['pk'])
        if todo.status==False:
            todo.status=True
            result='Done'
        else:
            todo.status=False
            result='Undone'
        todo.save()
        res = 'You have changed this item status as ' + result
        response = JsonResponse({'result' : res})
        return response


class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()



# class showitem(viewsets.ModelViewSet):

