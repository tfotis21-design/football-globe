from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    town = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    league = models.CharField(max_length=200, blank=True)
    stadium = models.CharField(max_length=200, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to="team_logos/", blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    colors = models.CharField(max_length=200, blank=True, help_text="e.g. Red & White")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
