# -*- coding: utf-8 -*- #
"""
product definition
"""


class Product():
    """ object constructor """

    def __init__(self, **product):
        self._columns_values = dict()
        self._columns_values['code'] = product['code'][0:100] \
            if 'code' in product else '0000000000000'
        self._columns_values['name'] = product['product_name'][0:300] \
            if 'product_name' in product else ''
        self._columns_values['generic_name'] = product['generic_name_fr'][0:200] \
            if 'generic_name_fr' in product else ''
        self._columns_values['brands'] = product['brands'][0:100] \
            if 'brands' in product else 'None'
        self._columns_values['stores'] = product['stores'][0:100] \
            if 'stores' in product else ''
        self._columns_values['url'] = product['url'] \
            if 'url' in product else ''
        self._columns_values['image_front_url'] = product['image_front_url'] \
            if 'image_front_url' in product \
            else 'dist/assets/img/nothing.png'
        self._columns_values['nutrition_grade'] = product['nutrition_grade_fr'] \
            if 'nutrition_grade_fr' in product else 'z'
        self._columns_names = \
            ['code', 'name', 'generic_name',
             'brands', 'stores', 'url',
             'image_front_url', 'nutrition_grade']

    # builder json
    @classmethod
    def buildfromjson(cls, **product):
        """ data from product """
        return cls(**product)

    # builder mysql
    @classmethod
    def buildfrommysql(cls, **product):
        """ data from mysql """
        # get 1 map from 2 with different origins => fusion with key change
        translation = {
            #           'code': 'code',
            'generic_name': 'generic_name_fr',
            'nutrition_grade': 'nutrition_grade_fr'}
        new_map = dict([
            ((k in translation and (translation.get(k))) or k, v)
            for k, v in product.items()])
        return cls(**new_map)

    def __str__(self):
        return str(self._columns_values)

    @property
    def ident(self):
        """ returns id product """
        return self._columns_values['id']

    @property
    def code(self):
        """ returns barcode  """
        return self._columns_values['code']

    @property
    def name(self):
        """ returns name """
        return self._columns_values['name']

    @property
    def generic_name(self):
        """ returns generic_name
        property openfactsfood """
        return self._columns_values['generic_name']

    @property
    def brands(self):
        """ returns brand names
        property openfactsfood """
        return self._columns_values['brands']

    @property
    def stores(self):
        """ returns store names
        property openfactsfood """
        return self._columns_values['stores']

    @property
    def url(self):
        """ returns url access
        property openfactsfood """
        return self._columns_values['url']

    @property
    def image_front_url(self):
        """ returns image url access
         """
        return self._columns_values['image_front_url']

    @property
    def nutrition_grade(self):
        """ returns nutrition grade
        property openfactsfood """
        return self._columns_values['nutrition_grade']

    @property
    def columns_names(self):
        """ returns dict of names """
        return self._columns_names

    @property
    def columns_values(self):
        """ returns dict of values """
        return self._columns_values
