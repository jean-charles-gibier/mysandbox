from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from product import models as prd
from substitute import models as sub


class ListProductsView(ListView):
    """
    Liste des produits (en premiere proposition
    après selection du mot clé. Pagination / 5
    Le mot clé est comparé aux champs respectivement
    nom de poduit  ou nom de catégorie
    """
    # chemin vers le template à afficher
    template_name = "product/query_products.html"
    model = prd.Product
    context_object_name = "produits_trouves"
    paginate_by = 5

    def get_queryset(self):
        my_query = self.request.GET.get("query")
        if my_query is not None:
            return prd.Product.objects.filter(
                Q(generic_name__icontains=my_query) |
                Q(brands__icontains=my_query))


class ListSubstitutesView(LoginRequiredMixin, ListView):
    """
    Affichage des produits substituables
    login requis
    Pagination / 6
    """
    # chemin vers le template à afficher
    template_name = "product/query_substitutes.html"
    login_url = '/user/login/'
    model = prd.Product
    context_object_name = "substituts_trouves"
    paginate_by = 6

    def get_queryset(self):
        idProduct = self.request.GET.get("id")
        if idProduct is not None:
            p_selection = prd.Product.objects.get(pk=idProduct)
            p_categories = p_selection.categories.all()
            p_nutrition_grade = p_selection.nutrition_grade

            lst_cat_id = ",".join([str(cat.id) for cat in p_categories])
            print('id product origin: {}'.format(idProduct))
            print('ids category: {}'.format(lst_cat_id))
            print('nutrition grade lesser the: {}'.format(p_nutrition_grade))

            list_prod = prd.Product.objects.filter(
                categories__in=p_categories,
                nutrition_grade__lt=p_nutrition_grade
            ).order_by('nutrition_grade')
            return list_prod

    def get_context_data(self, **kwargs):
        idProduct = self.request.GET.get("id")
        if idProduct is not None:
            p_selection = prd.Product.objects.get(pk=idProduct)
            ctx = super(ListSubstitutesView, self).get_context_data(**kwargs)
            ctx['product_name'] = p_selection.name
            ctx['brand_name'] = p_selection.brands
            ctx['image_front_url'] = p_selection.image_front_url
            return ctx


def register_subsituts(request):
    """
    Enregistre un substitut
    ie : établit une relaton ternaire produit / substitut / user
    :param request:
    :return: Http response
    """
    idProduct = request.GET.get("id")
    idSubstitute = request.GET.get("sub")
    p_origin = prd.Product.objects.get(pk=idProduct)
    p_substitute = prd.Product.objects.get(pk=idSubstitute)
#    created = 'No'

    try:
        sub.Substitute.objects.get(
            user_subst=request.user,
            product_origin=p_origin,
            product_substitute=p_substitute
        )

    except ObjectDoesNotExist:
        sub.Substitute.objects.create(
            user_subst=request.user,
            product_origin=p_origin,
            product_substitute=p_substitute
        )
#        created = 'Yes'

    reverse_url = reverse('home')
    messages.info(request, 'Selection enregisrée')
    return HttpResponseRedirect(reverse_url)
