from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name='landing'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("signup/", views.signup_user, name='signup'),
    path("home/", views.home, name='home'),
    path("music/", views.search_music, name='music'),
    path("friends/", views.search_friends, name='friends'),
]
