from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.db import connection

from apps.datagen.forms import PostForm, Taf_generar_form
from apps.datagen.models import TAF_table, Metar_trafico
# Create your views here.

#mostrando la pagina principal de mapgen
def view_mapa_index(request):
    if request.user.is_authenticated:
                #post=Flp_trafico.objects.raw("select * from p$
         metar=Metar_trafico.objects.raw("select * from plan_vuelo_flp_trafico where hora_amhs like '12%%%%' order by id_amhs desc ")
         return render(request, 'mapgen.html',{'metar':metar})
    else:
         return redirect('login')
#return render(request, 'mapgen.html')




def view_form_taf(request):
    if request.method == 'POST':
        form = Taf_generar_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('datagen/index.html')
    return render(request, 'datagen/temp_taf_form.html', {'form':Taf_generar_form.meta})

#showing the taf form
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            return render(request, 'datagen/index.html',{'form':form})
    else:
        form=PostForm()
        return render(request, 'datagen/post_edit.html', {'form':form})

def post_detail(request, pk):
    post = get_object_or_404(TAF_table, pk=pk)
    return render(request, 'datagen/post_detail.html',  {'post':post})





#MOSTRANDO OTRAS PAGINAS WEB
def view_pagina_generar(request):
    return render(request, 'generador.html')

def view_pagina_mapa(request):
    return render(request, 'mapgen.html')


def view_generador_index(request):
    return render(request, 'ico.html')
