from django.contrib import admin
from . models import Planets


class PlanetsAdmin(admin.ModelAdmin):
    fields = ['planet_number', 'planet_name']
    list_display = ('planet_number',
                    'planet_name',
                    'planet_mass_to_earth',
                    'satellites',)


admin.site.register(Planets)