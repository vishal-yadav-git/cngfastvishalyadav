from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import SignUpForm
from home import views

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')  # Return to login form if the method is GET or failed login







def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()  # Now the profile picture will be saved automatically with the user
            return redirect('login')  # Redirect to the login page or home page after successful signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

def index (request):
    return render (request, 'index.html')
    
def Product (request):
    return render (request, 'Product.html')

def Pricing (request):
    return render (request, 'Pricing.html')

def About (request):
    return render (request, 'About.html')

def Contect (request):
    return render (request, 'Contect.html')

def Page (request):
    return render (request, 'Page.html')