from typing import Any
from django.db.models.query import QuerySet
from django.views import generic

from offers.models import Category, Country, Offer


class IndexView(generic.ListView):
    context_object_name = "featured_offer_list"
    template_name = "offers/index.html"
    queryset = Offer.objects.filter(featured=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["featured_offer_list"] = Offer.objects.filter(featured=True)
        context["country_list"] = Country.objects.all()
        context["category_list"] = Category.objects.all()
        return context


class OfferListView(generic.ListView):
    model = Offer
    context_object_name = "offer_list"
    queryset = Offer.objects.all()


class OfferDetailView(generic.DetailView):
    model = Offer


class CountryDetailView(generic.DetailView):
    model = Country

    def get_context_data(self, **kwargs):
        context = super(CountryDetailView, self).get_context_data(**kwargs)
        context["offer_list"] = context["country"].offer_set.all()
        return context


class CategoryDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context["offer_list"] = context["category"].offer_set.all()
        return context
