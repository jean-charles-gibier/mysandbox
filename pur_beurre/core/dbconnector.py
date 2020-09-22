# -*- coding: utf-8 -*- #
"""
Connection stuff
 pg connector
"""
import json
import psycopg2
from django.conf import settings


class DbConnector(object):
    """ un instance = un handle"""
    def __init__(self, pathcfg=None):
        """ Init 1 connexion/session pour 1 objet DbConnector instancié """
        if pathcfg is not None:
            with open(pathcfg) as file_cfg:
                self._handle = psycopg2.connect(
                    **json.load(file_cfg)
                )
        else:
            test_cfg = getattr(settings, "DATABASES", None)
            if test_cfg is not None and 'default' in test_cfg:
                cfg = test_cfg['default']
                self._handle = psycopg2.connect(
                        dbname=cfg['NAME'],
                        user=cfg['USER'],
                        password=cfg['PASSWORD'],
                        host=cfg['HOST']
                    )

    def __del__(self):
        """ Au cas où """
        if hasattr(self, '_handle'):
            self._handle.close()
            delattr(self, '_handle')

    @property
    def handle(self):
        """ identifiant de session  """
        return self._handle
