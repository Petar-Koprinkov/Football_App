from django.shortcuts import render
from django.views.generic import ListView

from footballApplication.football.models import Countries


class HomeView(ListView):
    template_name = 'football/base.html'
    model = Countries
    context_object_name = 'countries'
    ordering = ['name']
