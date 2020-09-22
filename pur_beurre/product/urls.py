from django.urls import re_path

from .views import ListProductsView, ListSubstitutesView, register_subsituts

urlpatterns = [
    re_path(r"results?",
            ListProductsView.as_view(), name='query_products'),
    re_path(r"substitutes?",
            ListSubstitutesView.as_view(), name='query_substituts'),
    re_path(r"registersub?",
            register_subsituts, name='register_substituts'),
]
