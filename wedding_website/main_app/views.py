from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class Signup(View):
        # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("guestbook")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class Login(TemplateView):
    template_name = "login.html"


@method_decorator(login_required, name='dispatch') # block access if not registered
class Guestbook(TemplateView): #needs to be refactored into CRUD
    template_name = "guestbook.html"


@method_decorator(login_required, name='dispatch') # block access if not registered
class Accommodations(TemplateView): # good as is
    template_name = "accommodations.html"


@method_decorator(login_required, name='dispatch') # block access if not registered
class Schedule(TemplateView): #  good as is
    template_name = "schedule.html"


@method_decorator(login_required, name='dispatch') # block access if not registered
class Photos(TemplateView): # good as is
    template_name = "photos.html"


