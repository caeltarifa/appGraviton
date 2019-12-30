from django.conf.urls import url

from apps.datagen.views import view_form_taf, view_generador_index,post_new, view_pagina_generar, view_pagina_mapa

urlpatterns = [
    url(r'^$',view_generador_index, name='index_generador'),
    url(r'^formtaf/',view_form_taf, name='form_taf'),
    #url(r'^nuevo$',view_form_plan_vuelo, name='form_plan_vuelo'),
    url(r'^postnew/', post_new, name='post_new'),
    url(r'^generar/', view_pagina_generar, name='pagina_generar'),
    #url(r'^generar/', view_pagina_mapa, name='pagina_mapa'),
    #url(r'^postdetail/<int:pk>/', post_detail , name='post_detail'),
]