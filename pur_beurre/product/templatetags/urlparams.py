"""
trick picked from
https://stackoverflow.com/questions/51375759/django-url-template-with-query-parameters
"""
from django import template
import re

register = template.Library()


@register.simple_tag
def urlparams(query, todel):
    """
    suppress 'todel' parma from
    query string 'query'
    """
#    print(" urlparams appelé : '{}'  '{}'".format(query, todel))
    if query is None or todel is None:
        return ''
    new_query = re.sub(todel+"=[^&]*&?", '', query)
    new_query = re.sub("^\?$", '', new_query)
    new_query = re.sub("^&$", '', new_query)
#    print(" urlparams renvoyé : '{}'".format(new_query))
    return '{}'.format(new_query)
