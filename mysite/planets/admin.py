from django.contrib import admin
from . models import Planet, Moon


class MoonInLine(admin.TabularInline):
    model = Moon
    extra = 1
    list_display = ('planet_mother') # ???


class PlanetAdmin(admin.ModelAdmin):
    # fields = ['planet_number', 'planet_name']
    list_display = ('number',
                    'name',
                    'planet_mass_to_earth',
                    'orbital_speed',
                    'moons_quantity',
                    'image',)
    inlines = [MoonInLine]

admin.site.register(Planet, PlanetAdmin)
