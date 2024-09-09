from django.urls import path

from . import views

#it make namespace for the we can use like in html polls:view or polls:detail rather than usinf\g
# app_name = "polls"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/",views.detail,name="detail"),
#     path("<int:question_id>/results",views.results,name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
#  ]   

# pk is necessary because we going to use generic view
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), #as_view() calls itself
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]