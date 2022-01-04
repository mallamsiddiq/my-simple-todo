from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    context = { 'todos':todos}
    return render(request, 'home.html', context)

def details(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = { 'todo':todo, }
    return render(request, 'details.html', context)
def add(request):
    if request.method == 'POST':
        todo = Todo(title=request.POST['title'], body=request.POST['body'],execution_date=request.POST['execution_date'])
        todo.save()
        messages.success(request, 'Todo Added : %s' % todo.title)
        return redirect(reverse('todos:home'))
    else:
        return render(request, 'form.html')
def update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.body = request.POST['body']
        todo.execution_date = request.POST['execution_date']
        todo.save()
        messages.success(request, 'Todo Updated : %s' % todo.title)
        return redirect(reverse('todos:detail', args=[ id ]))
    else:
        context = { 'todo':todo, }
        return render(request, 'edit.html', context)
def delete(request, id):
    if (request.method == 'POST'):
        todo = get_object_or_404(Todo, pk=id)
        messages.success(request, 'Todo Deleted : %s' % todo.title)
        todo.delete()

    return redirect(reverse('todos:home'))
