from django.contrib import admin

from offers.models import Offer, Category, Country


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
