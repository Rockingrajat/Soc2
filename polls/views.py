'''from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404,render

def index(request):
    return HttpResponse("Hello User!You're at the polls index.This poll is regarding the best movie in recent times")
def detail(request,question_id):
    question=get_object_or_404(Question,pk=queston_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
     

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        except(KeyError,Choice.DoesNotExist):
            return render(request,'polls/detail.html'{
                'question':question,
                'error_message':"You didn't select a choice.",
                })
        else:
            selected_choice.votes+=1
            selected_choice.save()
            
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
# Create your views here.

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
        }
    return HttpResponse(template.render(context,request))

from django.http import Http404
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question Not Found")
        return render (request.'polls/detail.html',{'question':question})
    
#output=','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output) '''

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from django.utils import timezone 
from .models import Question,Choice

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
                'question':question,
                'error_message': "You didn't select a choice.",
                })
    else:
        selected_choice.votes+=1
        selected_choice.save()
            
        return HttpResponseRedirect(reverse('polls:index',))

    
