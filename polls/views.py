from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list' : latest_questions_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    return HttpResponse('You\'re looking question %s details' % question_id)

def results(request, question_id):
    return HttpResponse('You\'re looking question %s results' % question_id)

def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s' % question_id)
