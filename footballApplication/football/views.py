from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from footballApplication.football.models import Countries, Teams


class HomeView(View):
    def get(self, request):
        countries = Countries.objects.all()
        first_teams = Teams.objects.filter(position=1)

        context = {
            'countries': countries,
            'first_teams': first_teams

        }

        return render(request, 'football/base.html', context)