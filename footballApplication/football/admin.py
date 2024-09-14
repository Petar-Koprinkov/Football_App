from django.contrib import admin

from .models import Countries, Championship, Teams, Players


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'country__name')
    list_filter = ('country__name',)


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'titles', 'created_at', 'championship__name')
    list_filter = ('championship__name',)


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team__name',)
    list_filter = ('team__name',)






