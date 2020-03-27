from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TeacherIndex(request):
    return HttpResponse("This is index page of Teacher!")