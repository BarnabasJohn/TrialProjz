from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.order_by('id')
    form = TodoForm

    context = {'todos': todos, 'form': form}
    return render(request, 'todoapp/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteComplete(request):
    todo = Todo.objects.filter(complete__exact=True)
    todo.delete()
    todo.save()

    return redirect('index')


def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('index')
