"""
Composant du projet P5
filler est la classe chargée d'alimenter
 la base de donnée nativement
a partir du connecteur db msql ou pg
"""

from core import filler as fil
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    la commande filler alimente la base
    Parametre :
        nb_products
    10000 par defaut pour un calibrage
    adapté aux conditions d'heregement
    gratuit sur Heroku
    """
    help = 'Fills the current model via OFF'

    def add_arguments(self, parser):
        parser.add_argument('nb_products', nargs='?', type=int, default=10000)

    def handle(self, *args, **options):
        """ test filler is instancied """
        limit_nb_products = 0
        if 'nb_products' in options:
            limit_nb_products = options['nb_products']

        fil.Filler().start(limit_nb_products)
        pass
