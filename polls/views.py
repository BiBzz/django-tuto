from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest questions list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
	
class DetailsView(generic.DetailView):
	models = Question
	template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
	models = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {
			'question' : question,
			'error_message' : 'You didn\'t select a choice'
		})
	else:
		selected_choice.vote += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
