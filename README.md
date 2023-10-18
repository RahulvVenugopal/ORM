# Ex02 Django ORM Web Application
## Date: 18/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Footballplayer,FootballplayerAdmin
admin.site.register(Footballplayer,FootballplayerAdmin)

models.py
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

```

## OUTPUT
[Alt text](<Screenshot 2023-10-13 141808.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
