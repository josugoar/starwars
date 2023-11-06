from django.views import generic

from offers.models import Category, Country, Offer


class IndexView(generic.ListView):
    template_name = "offers/index.html"

    def get_queryset(self):
        return Offer.objects


class OfferView(generic.DetailView):
    model = Offer
    template_name = "offers/offer.html"


class CountryView(generic.DetailView):
    model = Country
    template_name = "offers/country.html"


class CategoryView(generic.DetailView):
    model = Category
    template_name = "offers/category.html"
