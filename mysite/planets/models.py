from django.db import models
import datetime


class CommonData(models.Model):
    name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField(primary_key=True)
    image = models.ImageField(blank=True, upload_to='planets/images/')
    discovery_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    wiki = models.URLField(blank=True)

    class Meta:
        abstract = True
        ordering = ['number']


class Planet(CommonData):
    planet_mass_to_earth = models.DecimalField(blank=True, max_digits=10, decimal_places=4, verbose_name='planet mass relative to an Earth')
    orbital_speed = models.DecimalField(blank=True, max_digits=5, decimal_places=3, verbose_name='Average orbital speed, km/s')
    moons_quantity = models.PositiveSmallIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = 'planet'
        verbose_name_plural = 'planets'

    def __str__(self):
        return self.name


class Moon(CommonData):
    planet_mother = models.ForeignKey(Planet, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'moon'
        verbose_name_plural = 'moons'

    def __str__(self):
        return str(self.planet_mother) + '--' + str(self.name)

