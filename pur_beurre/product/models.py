"""
product model definition
"""
from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    generic_name = models.CharField(max_length=200)
    brands = models.CharField(max_length=100)
    stores = models.CharField(max_length=100)
    url = models.URLField()
    image_front_url = models.URLField(default='')
    nutrition_grade = models.CharField(max_length=2)
    categories = models.ManyToManyField('Category', related_name='products')

    class Meta:
        verbose_name = "Produit"
        ordering = ['name']

    def __str__(self):
        """
        Cette méthode permet de definir l'entité product
        """
        return self.name


class Category(models.Model):
    tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name = "Categorie"
        ordering = ['name']

    def __str__(self):
        """
        Cette méthode permet de definir l'entité category
        """
        return self.name
