from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Todo


def home(request):
    todos = Todo.objects.filter(user=request.user)

    context = {'todos': todos}
    return render(request, 'todo/home.html', context)
