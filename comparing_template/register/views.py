from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import RegisterForm, UserEditForm, User

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
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'register/edit_profile.html', {'form': form})
    else:
        form = UserEditForm(instance=user)

    return render(request, 'register/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    user = User.username
    user.delete()

    return redirect('register')


