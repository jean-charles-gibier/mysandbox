# coding=utf-8
from core import dbconnector as dbc
from core import filler as fil
from core.dao import daoproduct as daop
from core.dao import daocategory as daoc
from django.test import TestCase


class CoreTestCase(TestCase):
    def setUp(self):
        """ fill db"""
        fil.Filler().start(10)


    def test_products_populated(self):
        """
        test if there products
        :return:
        """
        dao_product = daop.DaoProduct(name_table="product_product")
        self.assertIsNotNone(dao_product)
        dao_category = daoc.DaoCategory(name_table="product_category")
        self.assertIsNotNone(dao_category)

        prod = dao_product.get_id_product_by_ean("0000000000000")
        cat = dao_category.get_category_id("1")

#        nothing to do for now, (incompatibility pg/mysql)
#        except fix  this :
#           map_row = dict(zip(cursor.column_names, a_row))
#           AttributeError: 'psycopg2.extensions.cursor' object has no attribute 'column_names'

#        list_categories = dao_category.get_category_list()
#        list_products = dao_product.get_products_list_by_match('')
#        print ("Nb products : {} ".format(len(list_products)))
#        print ("Nb categories : {} ".format(len(list_categories)))
