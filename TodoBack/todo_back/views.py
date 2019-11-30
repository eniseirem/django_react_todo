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
        #check if any dependent todo exist
        dep_todos = TodoItem.objects.filter(dependency=kwargs['pk'])
        shouldUpdate = False
        if dep_todos.exists() == False:
            shouldUpdate = True
        else:
            parents = dep_todos.filter(status=False)
            #find dependent todos
            if parents.exists():
                deps = parents.values('name')
                explanation = 'This item depented on other todos, make done them before this one.'
                return JsonResponse({'explanation': explanation, 'todos': list(deps)}, status=401)
            else:
                shouldUpdate = True
        #change its status
        if(shouldUpdate):
            if todo.status==False:
                todo.status=True
                result='Done'
            else:
                todo.status=False
                result='Undone'
            todo.save()
            res = 'You have changed this item status as ' + result
            response = JsonResponse({'result': res})
            return response

class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

    @action(methods=['get'], detail=True)
    def items(self, *args, **kwargs):
        list_n= TodoList.objects.get(id=kwargs['pk'])
        todos = TodoItem.objects.filter(list=kwargs['pk']).values()
        return JsonResponse({'list_name' : list_n.title, 'todos' : list(todos)})


