from django.urls import path

from footballApplication.football.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]