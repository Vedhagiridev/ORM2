from django.db import models
from django.contrib import admin
class car1(models.Model):
    Car_name = models.CharField(max_length=255, help_text="Car name")
    Model = models.CharField(max_length=255, help_text="Model")
    Colour = models.CharField(max_length=255, help_text="Colour")
    
class car1Admin(admin.ModelAdmin):
    list_display = ('Car_name', 'Model', 'Colour')
