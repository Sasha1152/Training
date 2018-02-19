from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet


def planets_list(request):
    # return HttpResponse('Planets. The home page')
    planets = Planet.objects.all()
    # return HttpResponse(planets)
    return render(request, 'planets_list.html', {'planets': planets})


def planet_data(request, pk):
    planet = Planet.objects.get(pk=pk)
    # return HttpResponse(planet)
    return render(request, 'planet_data.html', {'planet': planet})


def page_1(request):
    return render(request, 'page_1.html')


def page_2(request):
    return HttpResponse("It's running function planet.views.page_2")