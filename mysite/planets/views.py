from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet, Moon
import datetime


def planets_list(request):
    # return HttpResponse('Planets. The home page')
    planets = Planet.objects.all()
    planets_some = Planet.objects.get(pk=7)
    moons = Moon.objects.all()
    # return HttpResponse(planets)
    now = datetime.datetime.now()
    return render(request, 'planets_list.html', {'planets': planets,
                                                 'moons': moons,
                                                 'now': now,
                                                 'planets_some': planets_some
                                                 })


def planet_data(request, name):
    planet = Planet.objects.get(name=name)
    moon = Moon.objects.get(name=name)
    # return HttpResponse(planet)
    return render(request, 'planet_data.html', {'planet': planet,
                                                'name': name,
                                                'moon': moon,
                                                })

def moon_data(request, name):
    moon = Moon.objects.get(pk=name)
    return render(request, 'planet_data.html', {'moon': moon, 'name': name})


