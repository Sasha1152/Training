from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet, Moon
import datetime


def planets_list(request):
    # return HttpResponse('Planets. The home page')
    planets = Planet.objects.all()
    moons = Moon.objects.all()
    # return HttpResponse(planets)
    now = datetime.datetime.now()
    return render(request, 'planets_list.html', {'planets': planets, 'moons': moons, 'now': now})


def planet_data(request, number):
    planet = Planet.objects.get(pk=number)
    # return HttpResponse(planet)
    return render(request, 'planet_data.html', {'planet': planet, 'number': number})

def moon_data(request, name):
    moon = Moon.objects.get(pk=name)
    return render(request, 'planet_data.html', {'moon': moon, 'name': name})


