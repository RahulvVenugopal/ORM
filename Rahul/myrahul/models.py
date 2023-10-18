from django.db import models
from django.contrib import admin
class Footballplayer(models.Model):
    name=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    age=models.IntegerField()
    experience=models.IntegerField()
    country=models.CharField(max_length=20)

class FootballplayerAdmin(admin.ModelAdmin):
    list_display=('name','role','age','experience','country')