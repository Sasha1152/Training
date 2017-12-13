from django.db import models


class Planets(models.Model):
    planet_number = models.PositiveSmallIntegerField(primary_key=True)
    planet_name = models.CharField(max_length=30)
    planet_mass_to_earth = models.DecimalField(blank=True, default=0, max_digits=10, decimal_places=4)
