from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(QuizQuestion)
admin.site.register(QuizInfo)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionOptions)
admin.site.register(ClassInfo)
admin.site.register(ClassEnrolled)