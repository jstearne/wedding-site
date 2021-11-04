from django.urls import path
from . import views

urlpatterns = [
    #path for home page
    path('', views.Home.as_view(), name="home"), 
]