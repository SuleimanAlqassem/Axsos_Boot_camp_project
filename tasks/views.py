from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm,ProjectForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required
def task_main(request):
    tasks = Task.objects.filter(owner=request.user, is_deleted=False).order_by('-created_at')
    return render(request, 'tasks/task_main.html',{'tasks': tasks})

@login_required
def ajax_task_list(request):
    tasks = Task.objects.filter(owner=request.user, is_deleted=False).order_by('-created_at')
    return render(request, 'tasks/partials/task_list.html', {'tasks': tasks})

@login_required
def ajax_task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST,user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TaskForm(user=request.user)
        return render(request, 'tasks/partials/task_form.html', {'form': form})
    
@login_required
def ajax_task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task,user=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TaskForm(instance=task,user=request.user)
        return render(request, 'tasks/partials/task_form.html', {'form': form, 'task': task})

@login_required
def ajax_task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.is_deleted = True
    task.save()
    return JsonResponse({'success': True})

@login_required
def ajax_task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    Status = Task.Status
    if task.status == Status.DONE:
        task.status = Status.TODO
    else:
        task.status = Status.DONE

    task.save()
    return JsonResponse({'success': True, 'new_status': task.status})

@login_required
def ajax_task_search(request):
    query = request.GET.get('q', '')
    tasks = Task.objects.filter(owner=request.user, title__icontains=query, is_deleted=False)
    return render(request, 'tasks/partials/task_list.html', {'tasks': tasks})


@login_required
def ajax_project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return JsonResponse({'success': True})
        else:
            html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = ProjectForm()
        html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

