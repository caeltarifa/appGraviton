from django.conf.urls import url

from apps.obs.views import view_observacion_index

urlpatterns = [
    url(r'^$',view_observacion_index, name='index_observacion'),
    #url(r'^formtaf/',view_form_taf, name='form_taf'),
    #url(r'^nuevo$',view_form_plan_vuelo, name='form_plan_vuelo'),
    #url(r'^postnew/', post_new, name='post_new'),
    #url(r'^generar/', view_pagina_generar, name='pagina_generar'),
    #url(r'^generar/', view_pagina_mapa, name='pagina_mapa'),
    #url(r'^postdetail/<int:pk>/', post_detail , name='post_detail'),
]