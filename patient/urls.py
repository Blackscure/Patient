from operator import add
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
#Native path to access the django admin
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.frontend, name="frontend"),

    # Path to login / logout
    path('login/', include('django.contrib.auth.urls')),

#----------------------- BACKEND SECTION -----------------------|
    # Path to access the backend page
    path('backend/',   views.backend, name="backend"),
    # Path to Add patient
    path('add_patient', views.add_patient, name="add_patient"),
]
