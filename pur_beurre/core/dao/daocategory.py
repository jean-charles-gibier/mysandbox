"""
Gestionnaire des data Category
"""
from core.dbconnector import DbConnector
from core.model.category import Category


class DaoCategory(object):
    """ definit les acces aux modele de donnees """

    def __init__(self, name_table="Category"):
        self.db = DbConnector()
        self.cnx = self.db.handle
        self.name_table = name_table

    def get_category_id(self, tag):
        """
        get a category id from his tag
        :param cnx: cnx handle
        :param tag: id openfoodfacts
        :return: Category
        """
        cursor = self.cnx.cursor()
        pre_sql = "SELECT id FROM {} WHERE tag = %s".format(self.name_table)
        cursor.execute(pre_sql, (tag,))
        cat_id = cursor.fetchone()
        cursor.close()
        return None if cat_id is None else cat_id[0]

    # def get_category_by_id(self, ident):
    #     """
    #     get a category object by his id
    #     :param id: pk
    #     :return: category product
    #     """
    #     category = None
    #     cursor = self.cnx.cursor()
    #     cursor.execute('SELECT * FROM %s WHERE id = %s',
    #                    (ident, self.name_table))
    #     a_row = cursor.fetchone()
    #     if a_row:
    #         map_row = dict(zip(cursor.column_names, a_row))
    #         category = Category.buildfrommysql(**map_row)
    #     cursor.close()
    #     return category
    #
    # def get_category_list(self, limit=100):
    #     """
    #     get a list of categorie (w.o condition)
    #     :return: list json of categories
    #     """
    #
    #     # list 2 return
    #     categories_list = list()
    #
    #     cursor = self.cnx.cursor()
    #
    #     # 1rst call we must determine string comparison
    #     comp_req = "SELECT * from %s " % (self.name_table,)
    #
    #     cursor.execute(comp_req)
    #
    #     for a_row in cursor:
    #         map_row = dict(zip(cursor.column_names, a_row))
    #         categories_list.append(Category.buildfrommysql(**map_row))
    #
    #     cursor.close()
    #     return categories_list
