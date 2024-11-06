# nuevoleonapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la vista index
        else:
            messages.error(request, 'Intentalo de nuevo ')
    return render(request, 'nuevoleonapp/login.html')

@login_required
def index(request):
    return render(request, 'nuevoleonapp/index.html')

def coahuila_view(request):
    return render(request, 'nuevoleonapp/Coahuila.html')

def sanluis_view(request):
    return render(request, 'nuevoleonapp/SanLuis.html')

def zacatecas_view(request):
    return render(request, 'nuevoleonapp/Zacatecas.html')

def datos_view(request):
    return render(request, 'nuevoleonapp/datos.html')
