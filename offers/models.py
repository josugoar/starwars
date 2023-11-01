from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Offer(models.Model):
    categories = models.ManyToManyField(Category, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.name)
