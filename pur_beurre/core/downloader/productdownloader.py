# coding: utf-8
"""
module de chargement des produits
"""

import logging as lg
import sys

from core import constant

logger = lg.getLogger(__name__)


class ProductDownloader(object):
    """ defines product object"""

    # collection of caotegorie
    _list_products = []

    """ Download products from OFF API """
    _page_counter = 1

    def reset_page_counter(self):
        """ reset page counter """
        self._page_counter = 1

    @property
    def nb_products(self):
        """ return nb fetched products """
        return len(self._list_products)

    @property
    def list_products(self):
        """ get page counter """
        return self._list_products

    @property
    def page_counter(self):
        """ get page counter """
        return self._page_counter

    def fetch(self, categorie, number=20):
        """ Fetch products from OFF API """
        # TODO : ajouter le champ 'image_front_url' => image
        from core.downloader.customrequest import special_get

        payload = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": categorie,
            "page_size": number,
            "page": self._page_counter,
            "fields": 'code,brands,url,stores,nutrition_grade_fr'
                      ',product_name,generic_name_fr,image_front_url',
            "json": 1
        }

        try:
            #            print("====> Appel  get
            #            products page : {}".format(self._page_counter))

            response = special_get(constant.API_URL_PRODUCTS, payload)
            #            print("====> Appel  get products page : Done")
            data = response.json()
            self._page_counter = self._page_counter + 1
            self._list_products = data['products']
        except:
            logger.error("Unexpected error:", sys.exc_info()[0])

        return len(self._list_products) > 0
