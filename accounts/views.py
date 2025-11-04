from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterForm, UserUpdateForm, ProfileForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # crea el Profile por si acaso
            Profile.objects.get_or_create(user=user)
            return redirect("profile_detail")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile_detail(request):
    return render(request, "accounts/profile_detail.html")

@login_required
def profile_edit(request):
    # ✅ garantiza que el perfil exista (a prueba de balas)
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect("profile_detail")
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=profile)

    return render(request, "accounts/profile_edit.html", {"uform": uform, "pform": pform})

def forgot_password(request):
    return render(request, "accounts/forgot_password.html")


