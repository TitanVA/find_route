from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from cities.forms import HtmlForm, CityForm
from cities.models import City


__all__ = (
    "home",
    "CityDetailView",
    "CityCreateView",
    "CityUpdateView",
)


def home(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    cities = City.objects.all()
    form = CityForm()
    context = {"cities": cities, "form": form}
    return render(request, "cities/home.html", context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail_city.html"


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = "cities/create.html"
    success_url = reverse_lazy("cities:home")

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy("cities:home")

