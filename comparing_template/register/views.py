from django.shortcuts import redirect
from django.shortcuts import render

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})
def about(request):
    return render(request, "main/about_us.html")
def features(request):
    return render(request, "main/features.html")
def homepage(request):
    return render(request, "main/home.html")
