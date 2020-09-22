"""
Give "greened" RGB color associated to nutriscrore letter
"""
from django import template

register = template.Library()


@register.simple_tag
def getcolor(nutriscore):
    """
    the more the note is close to 'A'
    the more the returned color looks green
    :param nutriscore:
    :return:
    """
    if nutriscore is None:
        return '#000000'
    value = ord((nutriscore.upper())[0]) - 65
    #    print('value {}'.format(value))
    vred = value * 50
    #    print('vred {}'.format(vred, 'x'))
    vgreen = 255 - (value * 50)
    #    print('vgreen {}'.format(vgreen, 'x'))

    return '#%02x%02x2080' % (vred, vgreen)
