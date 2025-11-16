from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def validate_signup_fields(request):
    username = request.GET.get('username', '')
    email = request.GET.get('email', '')
    password1 = request.GET.get('password1', '')
    password2 = request.GET.get('password2', '')
    response = {
        'username_exists': User.objects.filter(username=username).exists(),
        'email_exists': User.objects.filter(email=email).exists(),
        'password_match': password1 == password2,
        'password_strength': len(password1) >= 8 and any(c.isdigit() for c in password1),
    }
    return JsonResponse(response)



