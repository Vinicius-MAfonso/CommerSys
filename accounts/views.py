from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}! Conta criada com sucesso.")
            return redirect("core:index")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})
