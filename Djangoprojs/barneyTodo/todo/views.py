from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, DeleteView

from .models import Todo, Meet, Shopping
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
# pip package installation failure: python -m pip install --upgrade --force-reinstall pip


@login_required
def profile(request):

    user = request.user
    todos = Todo.objects.filter(author=request.user)
    shoppings = Shopping.objects.filter(author=request.user)
    meets = Meet.objects.filter(author=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account details have been updated ')
            return redirect('todo-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'todos': todos,
        'shoppings': shoppings,
        'meets': meets, 'user': user,
    }

    return render(request, 'todo/profile.html', context)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ShoppingCreateView(LoginRequiredMixin, CreateView):
    model = Shopping
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MeetCreateView(LoginRequiredMixin, CreateView):
    model = Meet
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def completeTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()

    return redirect('todo-profile')


def completeShopping(request, pk):
    shopping = Shopping.objects.get(id=pk)
    shopping.complete = True
    shopping.save()

    return redirect('todo-profile')


def completeMeet(request, pk):
    meet = Meet.objects.get(id=pk)
    meet.complete = True
    meet.save()

    return redirect('todo-profile')


def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('todo-profile')


def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('todo-profile')
