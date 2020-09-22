# coding=utf-8
"""
Test sur le parcours utilisateur
dans le choix des produits
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from product import models as prd
from substitute import models as sub


class ProductListTestCase  (TestCase):

    def setUp(self):
        """
        prepare some stuff for testing
        :return:
        """
        self.user_register = {
            'username': 'user_name',
            'email': 'name@free.fr',
            'password': 'Abcz1198!'
        }

        self.dummy_cat = prd.Category.objects.create(
            tag='tg0000',
            name='category 000',
            url='url000')

        self.p101 = prd.Product.objects.create(
            code='1000000000001',
            name='product 101',
            generic_name='A SUBSTITUER',
            brands='Coca',
            stores='stores001',
            url='url001',
            nutrition_grade='E')

        self.p102 = prd.Product.objects.create(
            code='1000000000002',
            name='product 102',
            generic_name='SUBSTITUTION',
            brands='Eau minerale',
            stores='stores001',
            url='url001',
            nutrition_grade='A')

        self.client = Client()
        self.user = User.objects.create(**self.user_register)
        self.user.save()

    def test_list_products_accessible(self):
        """ Verifie que la liste produit est accessible """
        response = self.client.get(reverse('query_products'),
                                   data={'query': 'A SUBSTITUER'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/query_products.html')

    def test_list_substitutes_not_accessible(self):
        """ Verifie que la liste des substituts est inaccessible """
        response = self.client.get(reverse('query_substituts'))
        self.assertEqual(response.status_code, 302)

    def test_list_substitutes_accessible(self):
        """ Verifie que la liste des substituts est accessible
            pour un user logué
        """
        self.user = User.objects.create_user(username='some_user',
                                             email='some_user@somewhere.com',
                                             password='Abcz1198!')
        self.client.login(username='some_user@somewhere.com',
                          password='Abcz1198!')
        response = self.client.get(reverse('query_substituts'))
        self.assertEqual(response.status_code, 200)

    def test_list_products_empty_with_bad_query(self):
        """ Verifie que la liste produit est vide avec un query inexistant """
        response = self.client.get(reverse('query_products'),
                                   data={'query': 'bière'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/query_products.html')

    def test_list_products_feed_with_good_query(self):
        """ Verifie que la liste produit remplie avec un query existant """
        response = self.client.get(reverse('query_products'),
                                   data={'query': 'Eau minerale'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/query_products.html')

    def test_create_substitute_for_identified_user(self):
         """ Verifie qu'un substitut peut être créé pour un user logué
         """
         self.user = User.objects.create_user(username='other_user',
                                              email='other_user@somewhere.com',
                                              password='Abcz1198!')
         self.client.login(username='other_user@somewhere.com', password='Abcz1198!')
         self.sub = sub.Substitute.objects.create(user_subst=self.user,
                                                  product_origin=self.p101,
                                                  product_substitute=self.p102)
         response = self.client.get(reverse('query_substituts'))
         self.assertEqual(response.status_code, 200)
