from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredients, Product
from .forms import Sozdanie_svechi
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    """" Главная страница"""
    return render(request, 'ingredients/index.html',)

def product_list(request, category_slug=None):
    """" Страница списка классов ингредиентов для свечи"""
    category = None
    ingredients = Ingredients.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Ingredients, slug=category_slug)
        products = products.filter(ingredients=category)
    context = {'category': category, 'ingredients': ingredients, 'products': products}
    return render(request, 'ingredients/list.html', context,)


def Ingredient_list(request, category_slug=None):
    """" Страница списка составляющих ингредиентов для каждого класса ингрединента"""
    category = None
    ingredients = Ingredients.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Ingredients, slug=category_slug)
        products = products.filter(ingredients=category)
    #""" Берем список компонентов и указывает отображение 9 на странице (метон пагинатор), затем получает номер страницы, и убираем исключения"""
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {"page_obj": page_obj, 'category': category, 'ingredients': ingredients, 'products': products, }
    return render(request, 'ingredients/Ingredient_list.html', context,)


def product_detail(request, id, slug):
    """ Страница описания каждого составляющего ингредиента"""
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {'product': product}
    return render(request, 'ingredients/detail.html', context,)

# Create your views here.
def sozdanie(request,):
    """" Страница с формой где мы выбираем составляющие свечи, а затем получаем свечу с описание ингредиентов"""
    products = Product.objects.all()
    location_list = Sozdanie_svechi()
    if request.method == "POST":
        # location_list = Sozdanie_svechi(request.POST)
        temp = request.POST['aroma']
        for product in products :
            if temp == product.name:
                 temp = product.slug
        temp1 = request.POST['kras']
        for product in products:
            if temp1 == product.name:
                temp1 = product.slug
        temp2 = request.POST['wosk']
        for product in products:
            if temp2 == product.name:
                temp2 = product.slug

        return redirect ('Svecha:res_svecha',temp,temp1,temp2)
    context = {
             'products': products,
             'location_list': location_list,
         }

    return render(request, "ingredients/sozdanie.html", context)



def res_svecha(request,slug, slug1, slug2):
    """ Страница c результатом получившейся свечи"""
    product1 = get_object_or_404(Product, slug = slug)
    product2 = get_object_or_404(Product, slug = slug1)
    product3= get_object_or_404(Product, slug=slug2)
    context = {'product1': product1, 'product2': product2, 'product3': product3,}
    return render(request, 'ingredients/res_svecha.html', context,)








# def sozdanie(request):
#     submitbutton = request.POST.get("Submit")
#     products = Product.objects.all()
#     location_list = Sozdanie_svechi(request.POST)
#     if location_list.is_valid():
#         temp = location_list.cleaned_data.get('aroma')
#         temp1 = location_list.cleaned_data.get('kras')
#         temp2 = location_list.cleaned_data.get('wosk')
#         context = {
#         'products': products,
#         'location_list': location_list,
#         'temp' : temp,
#         'temp1': temp1,
#         'temp2': temp2,
#         'submitbutton':submitbutton,
#         }
#     else:
#         context = {
#             'products': products,
#             'location_list': location_list,
#         }
#
#     return render(request, "ingredients/sozdanie.html", context)

