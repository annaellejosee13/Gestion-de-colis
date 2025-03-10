from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages






def login_user(request):
    if request.method =='POST':
        username_u = request.POST["username"]
        password_u = request.POST["password"]

        user =  authenticate(request, username = username_u, password = password_u)

        if user is not None:
            login(request, user)
            return redirect("colis:dashboard")
        else:
            messages.info(request, "Incorrect username or password")
    form = AuthenticationForm()
    return render(request, "accounts/login_a.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect("colis:index")

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("colis:index")
    else:
        form = UserCreationForm()
        
    return render(request, "accounts/register.html",{"form":form})