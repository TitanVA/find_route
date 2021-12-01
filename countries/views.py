from django.shortcuts import render
from django.views.generic import DetailView

from countries.models import Country


__all__ = (
    "home", "CountryDetailView"
)


def home(request):
    countries = Country.objects.all()
    context = {"countries": countries}
    return render(request, "countries/countries.html", context=context)


class CountryDetailView(DetailView):
    queryset = Country.objects.all()
    template_name = "countries/detail_country.html"
