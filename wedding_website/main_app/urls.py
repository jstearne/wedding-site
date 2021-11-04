from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('guestbook/', views.Guestbook.as_view(), name="guestbook"),
    path('accommodations/', views.Accommodations.as_view(), name="accommodations"),
    path('schedule/', views.Schedule.as_view(), name="schedule"),
    path('photos/', views.Photos.as_view(), name="photos"),
    path('login/', views.Login.as_view(), name="login"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]