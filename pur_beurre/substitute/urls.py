from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListRegisteredSubstitutes.as_view(),
         name='substitutes_list'),
    path('delete/', views.delete_substituts, name='delete_substituts'),
]
