from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse


from apps.datagen.models import Metar_trafico
# Create your views here.


def principal_presentacion(request):
    if request.user.is_authenticated:
        return redirect('despues_login')
    else:
        return redirect('login')


def despues_login(request):
    if request.user.is_authenticated:
        metar = Metar_trafico.objects.raw("select * from plan_vuelo_flp_trafico where hora_amhs like '12%%%%' order by id_amhs desc limit 20")
        return render(request, 'index.html', {'metar': metar})
        #return render(request, 'index.html')
    else:
        return redirect('login')

def denegar_login(request):
    return redirect ('despues_login')
