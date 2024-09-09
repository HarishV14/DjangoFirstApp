# from django.http import HttpResponse,Http404,HttpResponseRedirect
# from django.db.models import F

# from django.shortcuts import render,get_object_or_404

# from .models import Choice, Question

# from django.template import loader

# from django.urls import reverse


# def index(request):
#     # #it orders the questions stored by the date store in the list
#     #-pub_date indicates that descending order if put normal it will do like ascending order
#     latest_question_list=Question.objects.order_by("-pub_date")[:5]

#     # #It joins the value by , of only question_text which is stored in the above list
#     # output=",".join([q.question_text for q in latest_question_list])

#     #it is process of using the html template
#     # template = loader.get_template("polls/index.html") 

#     #this value should be used in the html page
#     context = {
#         "latest_question_list": latest_question_list,
#     }

#     #it used to render the the html page in this routes
#     # return HttpResponse(template.render(context, request))

#     #this another way of rendering the html page using shortcut in django
#     return render(request,"polls/index.html",context)
#     # return HttpResponse(output)

# def detail(request,question_id):

#     #try except is normal method that if pk as the given question_id then it render the questio
#     # try:
#         # question=Question.objects.get(pk=question_id)

#     #No means the except will call display 404 with question not exist message
#     # except:
#         # raise Http404("Question is Not exist")
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/detail.html",{"question":question})
#     # return HttpResponse("You'r looking at the result of question")



# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1 #instruct to database to increase the vote count by 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

from django.utils import timezone
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
        # return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 #instruct to database to increase the vote count by 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))