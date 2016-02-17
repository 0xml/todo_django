from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Project

def index(request):
    latest_projects_list = Project.objects.order_by('-pub_date')[:5]
    template = loader.get_template('todo/index.html')
    context = {
        'latest_projects_list': latest_projects_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    return HttpResponse("You're looking at question %s." % project_id)

def tasks(request, project_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % project_id)