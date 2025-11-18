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
]