from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppRegistro.forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

#Vista para el registro del usuario
def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            
            form.save()
            
            return redirect ("/")


    else:
        form = UserRegisterForm()

    return render(request, "AppRegistro/registro.html", {"form":form})

