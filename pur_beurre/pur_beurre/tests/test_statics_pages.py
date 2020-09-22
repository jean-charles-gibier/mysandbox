# coding=utf-8
"""
Test sur
l'accessibilité  générale
"""
from django.test import SimpleTestCase
from django.urls import reverse


class StaticPageTest(SimpleTestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pur_beurre/home.html')


class LegalNoticeTest(SimpleTestCase):
    def test_legal_notice_returns_200(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pur_beurre/legal_notice.html')
