from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class Guestbook(TemplateView): #needs to be refactored into CRUD
    template_name = "guestbook.html"

class Accomodations(TemplateView): # good as is
    template_name = "accomodations.html"

class Schedule(TemplateView): #  good as is
    template_name = "schedule.html"

class Photos(TemplateView): # good as is
    template_name = "photos.html"
