from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet


def home(request):
    # return HttpResponse('Planets. The home page')
    planets = Planet.objects.all()
    # return HttpResponse(planets)
    return render(request, 'planets/home.html', {'planets': planets})


def page_1(request):
    return render(request, 'planets/page_1.html')


def page_2(request):
    return HttpResponse("It's running function planet.views.page_2")