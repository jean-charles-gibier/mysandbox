# coding=utf-8
from core import dbconnector as dbc
from django.test import TestCase


class FillerTestCase(TestCase):
    def setUp(self):
        pass

    def test_filler_installation(self):
        """ test if db is responsive """
        # vérifie qu'il y a bien une db fonctionnelle
        pg_cnx = dbc.DbConnector()
        self.assertIsNotNone(pg_cnx.handle)


