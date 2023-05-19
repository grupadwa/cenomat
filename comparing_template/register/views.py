from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Przekierowanie na stronę logowania
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

