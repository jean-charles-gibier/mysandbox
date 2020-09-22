# -*- coding: utf-8 -*- #
"""
category definition
"""


class Category:
    """ category constructor """

    def __init__(self, **category):
        # petite verrue l'attribut id de off est renommé en tag
        self._columns_values = dict()
        self._columns_values['tag'] = category['id'] if 'id'\
                                                        in category else None
        self._columns_values['url'] = category['url'] if 'url'\
                                                         in category else None
        self._columns_values['name'] = category['name'] if 'name'\
                                                           in category else None
        self._columns_names = ['tag', 'url', 'name']

    # builder json
    @classmethod
    def buildfromjson(cls, **category):
        """ data from json"""
        return cls(**category)

    # builder mysql
    @classmethod
    def buildfrommysql(cls, **category):
        """ data from mysql"""
        return cls(**category)

    def __str__(self):
        """ express yourself"""
        return str(self._columns_values)

    @property
    def ident(self):
        """ should return id """
        return None

    @property
    def tag(self):
        """ returns openfactsfood id """
        return self._columns_values['tag']

    @property
    def name(self):
        """ returns off name """
        return self._columns_values['name']

    @property
    def columns_names(self):
        """ returns dict of names
        (each keys is the name of the element)"""
        return self._columns_names

    @property
    def columns_values(self):
        """ returns dict of values """
        return self._columns_values
