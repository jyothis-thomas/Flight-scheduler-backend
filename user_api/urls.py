from django.urls import path

from  user_api.views import  HelloView

urlpatterns = [
    path('home/', HelloView.as_view(), name='hello'),
]