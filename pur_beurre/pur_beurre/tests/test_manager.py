# coding=utf-8
"""
Check manager commands
"""

from product import models as prd
from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):
    """
    Check command efficiency
    """
    def test_filler(self):
        " Test filler command."

        args = ['10']
        opts = {}
        call_command('filler', *args, **opts)
        self.assertGreaterEqual(prd.Product.objects.count(), 10)

    def test_purge(self):
        " Test filler command."

        args = []
        opts = {}
        call_command('purge', *args, **opts)
        self.assertEqual(prd.Product.objects.count(), 0)


