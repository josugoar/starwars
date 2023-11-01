from django.contrib import admin
from offers.models import Offer, Category, Country

admin.site.register((Offer, Category, Country))
