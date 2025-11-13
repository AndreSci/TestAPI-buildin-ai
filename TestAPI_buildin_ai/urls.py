from django.contrib import admin
from django.urls import path
from main.views import home
from main.views import create_incident,get_incidents, update_incident_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('incidents/create/', create_incident),
    path('incidents/', get_incidents),
    path('incidents/update_status/', update_incident_status),
]