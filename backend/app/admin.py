from django.contrib import admin

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "league", "stadium", "founded_year")
    list_filter = ("country", "league")
    search_fields = ("name", "country", "league")
