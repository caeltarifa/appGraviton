from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.

def principal_presentacion(request):
    return render(request, 'index.html')