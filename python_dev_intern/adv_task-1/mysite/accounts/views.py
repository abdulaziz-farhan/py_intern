
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "form.html", {
        "form": form, "title": "Register"
    })


def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("home")

    return render(request, "form.html", {
        "form": form, "title": "Login"
    })


@login_required
def home(request):
    return render(request, "home.html")


def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("home")
