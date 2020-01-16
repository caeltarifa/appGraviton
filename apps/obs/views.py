from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.db import connection

# Create your views here.

#mostrando la pagina principal de observacion

def view_observacion_index(request):
    if request.user.is_authenticated:
        return render(request, 'observation/obs.html')
    else:
        return redirect('login')
