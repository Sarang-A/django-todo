from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    edit_task = None
    edit_id = request.GET.get('edit')

    if edit_id:
        edit_task = get_object_or_404(Task, pk=edit_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        # ➕ ADD TASK
        if action == 'add':
            title = request.POST.get('title')
            description = request.POST.get('description')
            due_date = request.POST.get('due_date')
            image = request.FILES.get('image')  # 🔥 important

            if title:
                Task.objects.create(
                    title=title,
                    description=description,
                    due_date=due_date if due_date else None,
                    image=image
                )

        # ✏️ EDIT TASK
        elif action == 'edit':
            pk = request.POST.get('pk')
            task = get_object_or_404(Task, pk=pk)

            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.due_date = request.POST.get('due_date') or None

            if request.FILES.get('image'):
                task.image = request.FILES.get('image')

            task.save()

        # ❌ DELETE TASK
        elif action == 'delete':
            pk = request.POST.get('pk')
            task = get_object_or_404(Task, pk=pk)
            task.delete()

        return redirect('task_list')

    return render(request, 'task_list.html', {
        'tasks': tasks,
        'edit_task': edit_task,
    })