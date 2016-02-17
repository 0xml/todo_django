from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(response):
	return HttpResponse("Todo application")

def detail(request, project_id):
    return HttpResponse("You're looking at question %s." % project_id)

def tasks(request, project_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % project_id)