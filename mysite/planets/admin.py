from django.contrib import admin
from . models import Planet


class PlanetAdmin(admin.ModelAdmin):
    # fields = ['planet_number', 'planet_name']
    list_display = ('planet_number',
                    'planet_name',
                    'planet_mass_to_earth',
                    'moons_quantity',
                    'planet_image',)


admin.site.register(Planet, PlanetAdmin)
