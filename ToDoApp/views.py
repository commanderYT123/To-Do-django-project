from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = TaskForm()
    context = {
        'form': form,
        'tasks':tasks,
    }
    return render(request, "pages/index.html", context)

def deletePage(request,pk):
    task = Task.objects.filter(pk=pk).first()
    context = {
        'task':task
    }
    return render(request,"pages/delete.html",context)


def delete(request,pk):
    task = Task.objects.filter(pk=pk).first()
    task.delete()
    return redirect('index')


def editPage(request,pk):
    task = Task.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'task':task,
        'form':form
    }
    return render(request,"pages/edit.html",context)

def toggle_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = not task.done
    task.save()
    return redirect('index')