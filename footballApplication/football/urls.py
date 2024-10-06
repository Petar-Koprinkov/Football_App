from django.urls import path
from footballApplication.football import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('team/<str:name>', views.TeamView.as_view(), name='team'),
    path('league/<str:name>', views.LeagueView.as_view(), name='league'),
    path('favourite/', views.FavoriteView.as_view(), name='favourite'),
]