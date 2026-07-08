from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def profile(request):
    return render(request, "profile.html")

def dashboard(request):
    content = {"content": "Hello Guest"}
    return render(request, "dashboard.html", content)

def login(request):
    return render(request, "login.html")