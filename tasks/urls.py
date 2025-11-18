from django.urls import path
from . import views

urlpatterns = [
    path('ajax/list/', views.ajax_task_list, name='ajax_task_list'),
    path('ajax/create/', views.ajax_task_create, name='ajax_task_create'),
    path('ajax/update/<int:pk>/', views.ajax_task_update, name='ajax_task_update'),
    path('ajax/delete/<int:pk>/', views.ajax_task_delete, name='ajax_task_delete'),
    path('ajax/toggle-status/<int:pk>/', views.ajax_task_toggle_status, name='ajax_task_toggle_status'),
    path('ajax/search/', views.ajax_task_search, name='ajax_task_search'),
    path('dashboard/', views.task_main, name='task_main'),
    path('ajax/project/create/', views.ajax_project_create, name='ajax_project_create'),
    path('projects/', views.project_main, name='project_main'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('note/add/<int:task_id>/', views.add_note, name='add_note'),
    path('trash/', views.task_trash, name='task_trash'),
    path('trash/restore/<int:pk>/', views.restore_task, name='restore_task'),
    path('trash/delete/<int:pk>/', views.delete_task_permanent, name='delete_task_permanent'),
    path('trash/empty/', views.empty_trash, name='empty_trash'),
    path('about/', views.about_page, name='about'),
    path('api/send-tasks-by-range/', views.send_tasks_by_range, name='send_tasks_by_range'),
    # path('api/send-today-tasks/', views.send_today_tasks, name='send_today_tasks'),
]