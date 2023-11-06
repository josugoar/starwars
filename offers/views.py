from django.views import generic

from offers.models import Category, Country, Offer


class IndexView(generic.ListView):
    template_name = "offers/index.html"

    def get_queryset(self):
        return Offer.objects


class OfferListView(generic.ListView):
    model = Offer
    context_object_name = "offer_list"
    queryset = Offer.objects


class OfferDetailView(generic.DetailView):
    model = Offer


class CountryDetailView(generic.DetailView):
    model = Country


class CategoryDetailView(generic.DetailView):
    model = Category
