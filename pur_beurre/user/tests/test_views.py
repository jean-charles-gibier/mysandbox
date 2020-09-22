# # coding=utf-8
# """
# Tests sur les vues user
# """
# from django.test import TestCase, Client
# from django.contrib.auth.models import AnonymousUser, User
# from django.test import RequestFactory, TestCase
# from user import view as vu
#
# class UserViewTestCase (TestCase):
#
#     def setUp(self):
#         """
#         setup creates needed user for testing user views
#         :return:
#         """
#         rf = RequestFactory()
#         post_request = rf.post('register/',
#                               {'username': 'foo',
#                                'email': 'foo@bar.com',
#                                'password1': 'ABCD1234',
#                                'password2': 'ABCD1234'
#                                })
#
#         vu.register(None)
#         self.client.login(username='foo@bar.coml', password='ABCD1234')
#         response = self.client.get(reverse('chistera:dashboard'))
#
#     def test_login_view(self):
#         """
#         check login
#         """
#         rf = RequestFactory()
#         get_request = rf.get('/login',
#                              {'username': 'foo@bar.com',
#                               'password': 'ABCD1234',
#                               }
#                              )
#         pprint.pprint(get_request)