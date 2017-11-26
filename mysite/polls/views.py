from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    text = 'Unfortunately, this Steve Jobs figurine may' \
           'not ship in time for the holidays'
    return HttpResponse(text)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
