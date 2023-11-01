from django.urls import path
from offers import views

urlpatterns = [
    path("", views.index, name="index"),
]
