from django.contrib import admin
from .models import Offer, Category, Country

admin.site.register((Offer, Category, Country))
