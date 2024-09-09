from django.urls import path

from . import views

#it make namespace for the we can use like in html polls:view or polls:detail rather than using
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/",views.detail,name="detail"),
    path("<int:question_id>/results",views.results,name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
 ]   