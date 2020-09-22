# coding: utf-8
"""
This package is imported from project #5
Adapted to Pgsql just 2 feed the db
"""
import logging as lg
from core import constant
from core.dao.daocategory import DaoCategory
from core.dao.writer import Writer
from core.downloader.categorydownloader import CategoryDownloader
from core.downloader.productdownloader import ProductDownloader
from core.model.category import Category
from core.model.product import Product

logger = lg.getLogger(__name__)

PRODUCT_PRODUCT = "product_product"
PRODUCT_CATEGORY = "product_category"
PRODUCT_CATEGORIES = "product_product_categories"
SUBSTITUTE_SUBSITUTES = "substitute_substitutes"


class Filler(object):
    """ classe en charge du chargement de la base """
    @classmethod
    def start(cls, nbmaxproducts=0):
        """ unique mehode de chargement """
        # remain nb of products to collect
        remain_nb_products = nbmaxproducts
        # instance de chargement des catégories
        category_downloader = CategoryDownloader()
        # instance de chargement des produits
        product_downloader = ProductDownloader()

        if not category_downloader.fetch(constant.DEFAULT_COUNTRY_ORIGIN,
                                         constant.LIMIT_NB_CATEGORIES):
            raise Exception("No category found for {} : Abort."
                            .format(constant.DEFAULT_COUNTRY_ORIGIN))

        logger.debug('Il y a %d categories à charger.',
                     category_downloader.nb_categories)
        category_writer = Writer(PRODUCT_CATEGORY)
        product_writer = Writer(PRODUCT_PRODUCT)
        product_category_writer = Writer(PRODUCT_CATEGORIES)

        logger.debug('Start collecting categories')
        category_writer.add_rows(category_downloader.list_categories, Category)
        logger.debug('End collecting categories')

        logger.debug('Start writing categories')
        category_writer.write_rows()
        logger.debug('End writing categories')

        # parcours des categories enregistrées
        logger.debug('Start collecting products')
        for category in category_downloader.list_categories:
            # break si on est au delà du nb de produits à collecter
            nb_products_to_load = \
                min([remain_nb_products, constant.LIMIT_NB_PRODUCTS])

            if nb_products_to_load < 0:
                break

            logger.debug('Start collecting category "%s"', category['name'])
            product_downloader.reset_page_counter()
            dao_category = DaoCategory(PRODUCT_CATEGORY)
            # get "our id" from "off id"
            category_id = dao_category.get_category_id(category['id'])

            # parcours des produits par catégories
            while product_downloader.fetch(category['name'],
                                           nb_products_to_load):
                logger.debug('Start getting page #%d',
                             product_downloader.page_counter - 1)
                # parcours des produits de la page courante
                new_list = product_writer.add_rows(
                    product_downloader.list_products, Product)

                # si une limite de de collecte a été indiquée
                if remain_nb_products > 0:
                    nb_collected = len(new_list)
                    if nb_collected > remain_nb_products:
                        new_list = new_list[:remain_nb_products]
                    remain_nb_products = remain_nb_products - nb_collected
                else:
                    break

#                print( "Nb code : {}".format(len(new_list)))
#                pprint.pprint(new_list[0])
#                bla = input("Get Key.")

                # ajout des index dans la table de jointure

                product_category_writer.add_rows(new_list,
                                                 {"product_id": '$code',
                                                  "category_id": category_id})
                logger.debug('End collecting category "%s"', category['name'])
                # Ecriture en base
                logger.debug('Start writing products')
#                bla = input("Before product_writer.write_rows().")
                product_writer.write_rows()

#                bla = input("After product_writer.write_rows().")
                logger.debug('End writing products')
                logger.debug('Start writing product_category relations')
                product_category_writer.join_rows(
                    "((select max(id) from " + PRODUCT_PRODUCT +
                    " where code ='{{product_id}}')," +
                    "{{category_id}})")
                logger.debug('End writing product_category relations')

                logger.debug('End getting page #%d',
                             product_downloader.page_counter - 1)
            logger.debug('End collecting category "%s"', category['name'])
        logger.debug('End collecting products')

    @classmethod
    def set_substitute_product(cls, pc_tuple):
        """  enregistre les liasons subistitut / produit """
        product_id, substitute_product_id = pc_tuple[0], pc_tuple[1]
        product_substitute = Writer(SUBSTITUTE_SUBSITUTES)
        product_substitute.add_rows({1}, {"product_id": product_id,
                                          "substitute_product_id":
                                              substitute_product_id})
        product_substitute.write_rows()
