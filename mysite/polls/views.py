from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

def index(request):
   latest_question_list = Question.objects.order_by("-pub_date")[:5]
   output = ",".join([q.question_text for q in latest_question_list])

    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
   context = {"latest_question_list": latest_question_list}   #return HttpResponse(template.render(context, request))
   return render(request, "index.html", context )

# def index(request):
#     return HttpResponse("Hello, world. Your're at the polls index")
# Create your views here.
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)