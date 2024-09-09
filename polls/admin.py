from django.contrib import admin

# Register your models here.
from . models import Question,Choice



#it gives stack inline
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

#it gives the tabular inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #it add the search field
    search_fields = ["question_text"]
    # fields = ["pub_date", "question_text"]
    #it adds the filter 
    list_filter = ["pub_date"]
    # it make the listing question format
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}), #First parameter is mentioning the fild name and none mentions that should be no heading field
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}), #classes collapse made that fild as hide and then clicking arrow it opens
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)


admin.site.register(Choice)
