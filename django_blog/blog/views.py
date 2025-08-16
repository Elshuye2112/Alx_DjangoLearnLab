# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'blog/login.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

# Profile view
@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
            messages.success(request, "Profile updated successfully.")
    return render(request, 'blog/profile.html')
