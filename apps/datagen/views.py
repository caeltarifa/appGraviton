from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

from apps.datagen.forms import PostForm, Taf_generar_form
from apps.datagen.models import TAF_table
from apps.mapgen.views import view_mapa_index
# Create your views here.

#mostrando la pagina principal de datagen
def view_generador_index(request):
    return render(request, 'datagen/index.html')

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
