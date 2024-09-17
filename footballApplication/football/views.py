from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from footballApplication.football.models import Countries, Teams


class HomeView(View):
    def get(self, request):
        countries = Countries.objects.all()
        first_teams = Teams.objects.filter(position=1)
        uefa_teams = Teams.objects.filter(european_title__icontains='UEFA')

        context = {
            'countries': countries,
            'first_teams': first_teams,
            'uefa_teams': uefa_teams
        }

        return render(request, 'football/index.html', context)


class LeagueView(View):
    def get(self, request, name):
        country = Countries.objects.get(name=name)
        league = country.championships.first()
        teams = league.teams.all()

        context = {
            "league": league,
            "teams": teams
        }
        return render(request, 'football/leagues.html', context)
