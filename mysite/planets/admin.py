from django.contrib import admin
from . models import Planets


class PlanetsAdmin(admin.ModelAdmin):
    fields = ['planet_number', 'planet_name', 'planet_mass']


admin.site.register(Planets)