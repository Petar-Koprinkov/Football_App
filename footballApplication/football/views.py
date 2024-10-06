from django.shortcuts import render, redirect
from django.views import View

from footballApplication.football.forms import CommentForm
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


class TeamView(View):
    def get(self, request, name):
        team = Teams.objects.get(name=name)
        favourite_teams = request.session.get('favourite_teams', [])
        is_favourite = team.id in favourite_teams
        form = CommentForm()

        context = {
            "form": form,
            "team": team,
            "is_favourite": is_favourite
         }

        return render(request, 'football/team.html', context)

    def post(self, request, name):
        team = Teams.objects.get(pk=int(name))
        form = CommentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data:
                comment = form.save(commit=False)
                comment.team = team
                comment.save()

        return redirect('team', team.name)


class FavoriteView(View):

    def get(self, request):
        favourite_teams = request.session.get('favourite_teams')
        context = {}

        if not favourite_teams:
            context['favourite_teams'] = []
            context['is_favourite'] = False
        else:
            teams = Teams.objects.filter(id__in=favourite_teams)
            context['is_favourite'] = True
            context['favourite_teams'] = teams

        return render(request, 'football/favourite.html', context)

    def post(self, request):
        favourite_teams = request.session.get('favourite_teams', [])

        team_id = int(request.POST.get('team_id'))

        if team_id not in favourite_teams:
            favourite_teams.append(team_id)
        else:
            favourite_teams.remove(team_id)
        request.session['favourite_teams'] = favourite_teams

        return redirect('home')
