from django.urls import path
from offers import views

app_name = "offers"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.OfferView.as_view(), name="offer"),
    path("countries/<int:pk>/", views.CountryView.as_view(), name="country"),
    path("categories/<int:pk>/", views.CategoryView.as_view(), name="category"),
]
