from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.

def index(request):
	latest_questions_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_questions_list' : latest_questions_list}
	return render(request, 'polls/index.html', context)

def details(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', { 'question' : question })

def results(request, question_id):
	return HttpResponse('You\'re looking question %s results' % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls:details', {
			'question_id' = question_id,
			'error_message' = 'You didn\'t select a choice'
		})
	else.
		selected_choice.vote += 1
		selected_choice.save()
	return render(request, 'polls:vote', { 'question_id' : question_id })
