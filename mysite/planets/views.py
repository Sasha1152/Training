from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet
import datetime


def planets_list(request):
    # return HttpResponse('Planets. The home page')
    planets = Planet.objects.all()
    earth = Planet.objects.get(pk=3)
    # return HttpResponse(planets)
    now = datetime.datetime.now()
    return render(request, 'planets_list.html', {'planets': planets, 'now': now})


def planet_data(request, number):
    planet = Planet.objects.get(pk=number)
    # return HttpResponse(planet)
    return render(request, 'planet_data.html', {'planet': planet, 'number': number})

