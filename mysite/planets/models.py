from django.db import models
import datetime


class CommonData(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='planets/images/')
    discovery_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    wiki = models.URLField(blank=True)

    class Meta:
        abstract = True


class Planet(CommonData):
    number = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    planet_mass_to_earth = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4, verbose_name='Planet mass relative to an Earth')
    orbital_speed = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=3, verbose_name='Average orbital speed, km/s')
    moons_quantity = models.PositiveSmallIntegerField(blank=True, default=0)

    class Meta:
        ordering = ['number']
        verbose_name = 'planet'
        verbose_name_plural = 'planets'

    def __str__(self):
        return self.name


class Moon(CommonData):
    name = models.CharField(max_length=30, primary_key=True)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='moons')
    number = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['number']
        verbose_name = 'moon'
        verbose_name_plural = 'moons'

    def __str__(self):
        return str(self.planet) + '--' + str(self.name)
