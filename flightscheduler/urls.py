from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    # path('', include('flights.urls')),
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls')),
]
