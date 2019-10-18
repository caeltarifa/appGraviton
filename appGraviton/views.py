from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.

def principal_presentacion(request):
    if request.user.is_authenticated:
        return redirect( 'despues_login')
    else:
        return redirect('login')

def despues_login (request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')

def denegar_login(request):
        return redirect ('despues_login')