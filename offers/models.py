from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Offer(models.Model):
    categories = models.ManyToManyField(Category)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
