# coding=utf-8
"""
Test de la commande d'administration filler
"""
from django.test import TestCase
from product import models as prd
from core import filler as fil


class FillerTestCase(TestCase):
    def setUp(self):
        """ nothing at the moment """
        pass

    def test_filler_start(self):
        """ test if filler works and model is instancied """
        fil.Filler().start(10)
        # vérifie qu'il y a bien 10 objets dans le model product
        self.assertGreaterEqual(prd.Product.objects.count(), 10)

