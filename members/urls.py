from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name='landing'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("signup/", views.signup_user, name='signup'),
    path("home/", views.home, name='home'),
    path('music/', views.search_music, name='music'),
    path('save_track/', views.save_track, name='save_track'),
    path('remove_track/<int:track_id>/', views.remove_track, name='remove_track'),
    path("friends/", views.search_friends, name='friends'),
    path('add_friend/<int:friend_id>/', views.add_friend, name='add_friend'),
    path('remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
]
