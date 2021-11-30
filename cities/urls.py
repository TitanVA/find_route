from django.contrib import admin
from django.urls import path

from cities.views import *

urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>/', home, name="detail_city"),
]
