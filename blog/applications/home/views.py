import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

# import apps
from applications.entrada.models import Entry

class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # contexto de entrada en portada
        context['portada'] = Entry.objects.entrada_en_portada()
        
        # contexto de entradas en Home
        context['entradas_home'] = Entry.objects.entradas_en_home()

        # contexto de entradas en Home
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        return context
    

