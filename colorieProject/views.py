from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *



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

def subscribe(request):
    if request.method == "POST":
        email = request.POST["email"]
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, "This email already exists, try another one")
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, "You have successfully subscribed")
            return redirect("subscribe")
    return render(request, "subscribe.html")


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            return redirect("blogs")
    else:
        form = BlogForm()
    return render(request, "add_blog.html", {"form": form})


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)