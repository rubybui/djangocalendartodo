# cal/urls.py

from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]

"""
This is wrong
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
"""
