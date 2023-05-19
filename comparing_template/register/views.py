from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return HttpResponse(render(response, "register/register.html", {"form": form}))
