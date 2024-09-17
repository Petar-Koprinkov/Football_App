from django.urls import path

from footballApplication.football.views import HomeView, LeagueView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('league/<str:name>', LeagueView.as_view(), name='league'),
]