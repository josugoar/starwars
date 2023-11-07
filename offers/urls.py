from django.urls import path
from offers import views

app_name = "offers"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("offers/", views.OfferListView.as_view(), name="offer-list"),
    path("offers/<int:pk>/", views.OfferDetailView.as_view(), name="offer-detail"),
    path("countries/<int:pk>/", views.CountryDetailView.as_view(), name="country-detail"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
]
