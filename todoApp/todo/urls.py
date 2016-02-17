from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /todo/
    url(r'^$', views.index, name='index'),
    # ex: /todo/5/
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /todo/5/tasks/
    url(r'^(?P<project_id>[0-9]+)/tasks/$', views.results, name='tasks'),
]