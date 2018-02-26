from django.http import HttpResponse
from . models import Question, Choice
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # return HttpResponse(', '.join([q.question_text for q in latest_question_list])) #2 remove
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list}) #2 add

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)