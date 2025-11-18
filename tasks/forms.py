from django import forms
from .models import Task,Project

class TaskForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        user=kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(owner=user)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status','project']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description',
                'rows': 3
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'project': forms.Select(attrs={
                'class': 'form-select'
                }),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'status': 'Status',
            'project':'Project',
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }