from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    edit_task = None
    edit_id = request.GET.get('edit')

    if edit_id:
        edit_task = get_object_or_404(Task, pk=edit_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        # Add new task
        if action == 'add':
            title = request.POST.get('title')
            if title:
                Task.objects.create(title=title)

        # Save edited task
        elif action == 'edit':
            pk = request.POST.get('pk')
            task = get_object_or_404(Task, pk=pk)
            task.title = request.POST.get('title')
            task.save()

        # Delete task
        elif action == 'delete':
            pk = request.POST.get('pk')
            task = get_object_or_404(Task, pk=pk)
            task.delete()

        return redirect('task_list')

    return render(request, 'task_list.html', {'tasks': tasks, 'edit_task': edit_task,})