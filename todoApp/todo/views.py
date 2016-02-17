from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Project

def index(response):
    latest_projects_list = Project.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.project_name for p in latest_projects_list])
    return HttpResponse(output)

def detail(request, project_id):
    return HttpResponse("You're looking at question %s." % project_id)

def tasks(request, project_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % project_id)