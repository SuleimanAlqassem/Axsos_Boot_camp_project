from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    """
    This view renders the homepage for authenticated users.
    It serves as the entry point to the Smart Task Manager dashboard.
    """
    return render(request, 'home.html')