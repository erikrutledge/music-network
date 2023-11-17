from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages
from . import index
from .models import Track, Profile


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
    return render(request, 'home.html')


def search_friends(request):
    context = {}
    User = get_user_model()
    search_query = request.GET.get('q')

    current_user_profile = Profile.objects.get(user=request.user)  
    user_friends = current_user_profile.friends.all()

    if search_query:
        users = Profile.objects.filter(Q(username__icontains=search_query) & ~Q(user__in=user_friends)).exclude(pk=request.user.id)
    else:
        users = Profile.objects.exclude(pk=request.user.id).exclude(user__in=user_friends)
    context['users'] = users
    context['query'] = search_query

    return render(request, 'search_friends.html', context)

def add_friend(request, friend_id):
    User = get_user_model()
    friend = User.objects.get(pk=friend_id)

    # Create friend relation between profiles
    current_user_profile = Profile.objects.get(user=request.user)
    current_user_profile.friends.add(friend)
    current_user_profile.save()

    return redirect('home')

def remove_friend(request, friend_id):
    User = get_user_model()
    friend = User.objects.get(pk=friend_id)
    print(friend.username)

    # Remove friend relation between profiles
    current_user_profile = Profile.objects.get(user=request.user)
    current_user_profile.friends.remove(friend)
    current_user_profile.save()

    return redirect('home')


def search_music(request):
    context = {}
    search_query = request.GET.get('q', '')

    if search_query:
        response = index.getTrack(search_query)
        context['response'] = response
        context['query'] = search_query

        return render(request, 'search_music.html', context)

    else:
        return render(request, 'music_landing.html', context)

def save_track(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        url = request.POST.get('url')
        img = request.POST.get('img')

        # DETERMINE IF THE TRACK IS ALREADY CREATED IN THE DATABASE, ONLY CREATE IF NOT EXISTING
        track_object = Track.objects.filter(title=title, artist=artist, url=url, img=img).first()
        if track_object:
            print("TRACK ALREADY EXISTS")
            pass
        else:
            # Create the new track object
            print("CREATING NEW TRACK OBJECT")
            track_object = Track.objects.create(title=title, artist=artist, url=url, img=img)

        # Associate the track object to the user
        track_object.username.add(request.user)
        track_object.save()
        
        # Associate the track object to the 'tracks' variable of the current user's Profile model
        current_user_profile = Profile.objects.get(user=request.user)
        current_user_profile.tracks.add(track_object)
        current_user_profile.save()
        
    return redirect('home')

def remove_track(request, track_id):
    current_user_profile = Profile.objects.get(user=request.user)
    track = get_object_or_404(Track, id=track_id)

    current_user_profile.tracks.remove(track)
    current_user_profile.save()

    return redirect('home')
