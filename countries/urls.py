from django.urls import path
from countries.views import *


urlpatterns = [
    path("", home, name="home"),
    path("detail/<int:pk>", CountryDetailView.as_view(), name="detail")
]
