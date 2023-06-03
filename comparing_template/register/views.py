from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserEditForm, UserDeleteForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})


@login_required
def edit_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserEditForm(instance=user)
        return render(request, 'register/edit_user.html', {'form': form})

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'register/edit_user.html', {'form': form})



@login_required
def delete_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserDeleteForm()
        return render(request, 'register/delete_user.html', {'form': form})

    if request.method == 'POST':
        user.delete()

        return redirect('login')


def about(request):
    return render(request, "main/about_us.html")


def features(request):
    return render(request, "main/features.html")


def homepage(request):
    return render(request, "main/home.html")


