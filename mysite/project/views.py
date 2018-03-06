from django.shortcuts import render
from django.http import HttpResponse
import datetime


def homepage(request):
    # return HttpResponse("<h1>It's home page</h1>")
    return render(request, 'homepage.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
