from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet

def home(request):
	# return HttpResponse('Planets. The home page')
	planets = Planet.objects.all()
	# return HttpResponse(planets)
	return render(request, 'home.html', {'planets': planets})