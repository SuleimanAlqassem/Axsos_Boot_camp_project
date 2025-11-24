from django.shortcuts import render, redirect, get_object_or_404
from .models import Task,Project,Note
from .forms import TaskForm,ProjectForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from .utils.email import send_task_summary_email
from .utils.email import send_task_created_email
from django.utils import timezone
from datetime import datetime, time


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
            #using Gmail API for sending Email
            send_task_created_email(request.user.email, task)
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
            html = render_to_string('tasks/partials/project_card.html', {'project': project})
            return JsonResponse({'success': True,'html': html})
        else:
            html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = ProjectForm()
        html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

@login_required
def project_main(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'tasks/project_main.html', {'projects': projects})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    notes = Note.objects.filter(task=task).order_by('-updated_at')
    return render(request, 'tasks/task_detail.html', {'task': task, 'notes': notes})

@login_required
def add_note(request, task_id):
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Note.objects.create(task=task, content=content,author=request.user)
    return redirect('task_detail', pk=task.id)

@login_required
def task_trash(request):
    tasks = Task.objects.filter(owner=request.user, is_deleted=True).order_by('-updated_at')
    return render(request, 'tasks/task_trash.html', {'tasks': tasks})

@login_required
def restore_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user, is_deleted=True)
    task.is_deleted = False
    task.save()
    return redirect('task_trash')

@login_required
def delete_task_permanent(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user, is_deleted=True)
    task.delete()
    return redirect('task_trash')

@login_required
def empty_trash(request):
    Task.objects.filter(owner=request.user, is_deleted=True).delete()
    return redirect('task_trash')

@login_required
def about_page(request):
    return render(request, 'tasks/about.html')

# Gmail API

@login_required
def send_today_tasks(request):
    today = timezone.now().date()
    start = datetime.combine(today, time.min)
    end = datetime.combine(today, time.max)
    tasks = Task.objects.filter(owner=request.user, updated_at__range=(start, end))

    if tasks.exists():
        send_task_summary_email(request.user.email, tasks)
        return JsonResponse({'success': True, 'message': 'Email sent successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'No tasks for today'})

@login_required
def send_tasks_by_range(request):
    if request.method == 'POST':
        start_str = request.POST.get('start')
        end_str = request.POST.get('end')

        try:
            start = datetime.fromisoformat(start_str)
            end = datetime.fromisoformat(end_str)
        except Exception:
            return JsonResponse({'success': False, 'message': 'Invalid date format'})

        tasks = Task.objects.filter(owner=request.user, updated_at__range=(start, end))

        if tasks.exists():
            send_task_summary_email(request.user.email, tasks)
            return JsonResponse({'success': True, 'message': 'Email sent successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No tasks in selected range'})
        
@login_required
def ajax_project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project=form.save()
            html = render_to_string('tasks/partials/project_card.html', {'project': project}, request=request)
            return JsonResponse({'success': True,'html': html})
        else:
            html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})

    # GET — إعادة النموذج داخل المودال
    form = ProjectForm(instance=project)
    html = render_to_string('tasks/partials/project_form.html', {'form': form}, request=request)
    return JsonResponse({'html': html})


@login_required
def ajax_project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    project.delete()
    return JsonResponse({'success': True})