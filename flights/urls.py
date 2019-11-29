
from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

urlpatterns = [   
    # url(r'^$', views.HomePageView.as_view()),

    url(r'^(?P<pk>[0-9]*)$', views.flight_detail),
    url(r'^$', views.flight_list)
]
