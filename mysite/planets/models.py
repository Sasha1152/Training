from django.db import models


class Planets(models.Model):
    planet_number = models.PositiveSmallIntegerField(primary_key=True)
    planet_name = models.CharField(max_length=30)
    planet_mass_to_earth = models.DecimalField(blank=True, max_digits=10, decimal_places=4, verbose_name='planet mass relative to an Earth')
    moons_quantity = models.PositiveSmallIntegerField(blank=True, default=0)
    planet_image = models.ImageField(blank=True)
    planet_description = models.TextField(blank=True)

    class Meta:
        ordering = ['planet_number']
        verbose_name = 'planet'
        verbose_name_plural = 'planets'

    def __str__(self):
        return self.planet_name


class Moons(models.Model):
    planet_mother = models.ForeignKey(Planets, on_delete=models.CASCADE)
    moon_number = models.PositiveSmallIntegerField(primary_key=True)
    moon_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['moon_number']
        verbose_name = 'moon'
        verbose_name_plural = 'moons'

    def __str__(self):
        return self.planet_mother + '--' + self.moon_name

