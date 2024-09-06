from django.http import HttpResponse,Http404

from django.shortcuts import render,get_object_or_404

from .models import Question

from django.template import loader


def index(request):
    # #it orders the questions stored by the date store in the list
    #-pub_date indicates that descending order if put normal it will do like ascending order
    latest_question_list=Question.objects.order_by("-pub_date")[:5]

    # #It joins the value by , of only question_text which is stored in the above list
    # output=",".join([q.question_text for q in latest_question_list])

    #it is process of using the html template
    # template = loader.get_template("polls/index.html") 

    #this value should be used in the html page
    context = {
        "latest_question_list": latest_question_list,
    }

    #it used to render the the html page in this routes
    # return HttpResponse(template.render(context, request))

    #this another way of rendering the html page using shortcut in django
    return render(request,"polls/index.html",context)
    # return HttpResponse(output)

def detail(request,question_id):

    #try except is normal method that if pk as the given question_id then it render the questio
    # try:
        # question=Question.objects.get(pk=question_id)

    #No means the except will call display 404 with question not exist message
    # except:
        # raise Http404("Question is Not exist")
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})
    # return HttpResponse("You'r looking at the result of question")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


