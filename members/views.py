from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Track, Profile
from . import index

def landing(request):
    return render(request, 'landing.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in. Please try again."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successful."))
    return redirect('landing')

def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful."))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/signup.html', {'form': form})




def home(request):
    data = Track.objects.filter(username = request.user)
    return render(request, 'home.html', {'tracks': data})

def search_friends(request):
    User = get_user_model()
    data = User.objects.all()
    return render(request, 'search_friends.html', {'users': data})

def search_music(request):
    search_query = request.GET.get('search_query', None)
    if search_query:
        response = index.getTrack(search_query)

        return render(request, 'search_music.html', {'tracks': response})
    else:
        return render(request, 'music_landing.html')