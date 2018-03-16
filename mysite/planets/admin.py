from django.contrib import admin
from . models import Planet, Moon


class MoonInLine(admin.TabularInline):
    model = Moon
    extra = 1
    list_display = 'planet_mother'  # ???


class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'name',
        'planet_mass_to_earth',
        'mean_radius_to_earth',
        'semi_major_axis',
        'orbital_speed',
        'orbital_period',
        'rotation_period',
        'escape_velocity',
        'surface_gravity',
        'surface_pressure',
        'moons_quantity',
        'discovery_date',
        'image',
        'symbol',

    )
    inlines = [MoonInLine]

admin.site.register(Planet, PlanetAdmin)
