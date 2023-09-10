from django.shortcuts import render, get_object_or_404
from .models import Ingredients, Product
from .forms import Sozdanie_svechi

def product_list(request, category_slug=None):
    """" Страница списка составляющих"""
    category = None
    ingredients = Ingredients.objects.all()
    products = Product.objects.all() #filter(ingredients=[i for i in ingredients])
    if category_slug:
        category = get_object_or_404(Ingredients, slug=category_slug)
        products = products.filter(ingredients=category)
    context = {'category': category, 'ingredients': ingredients, 'products': products}
    return render(request, 'ingredients/list.html', context,)


def product_detail(request, id, slug):
    """ Страница ингредиента"""
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {'product': product}
    return render(request, 'ingredients/detail.html', context,)

def ing(request, category_slug=None):
    """" Страница списка составляющих"""
    category = None
    ingredients = Ingredients.objects.all()
    products = Product.objects.all() #filter(ingredients=[i for i in ingredients])
    if category_slug:
        category = get_object_or_404(Ingredients, slug=category_slug)
        products = products.filter(ingredients=category)
    context = {'category': category, 'ingredients': ingredients, 'products': products}
    return render(request, 'ingredients/ing.html', context,)



# Create your views here.
def sozdanie(request,):
    temp =None
    temp1 = None
    temp2 = None
    products = Product.objects.all()
    location_list = Sozdanie_svechi()
    if request.GET:
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
        context = {
        'products': products,
        'location_list': location_list,
        'temp' : temp,
        'temp1': temp1,
        'temp2': temp2,
        }
    else:
        context = {
            'products': products,
            'location_list': location_list,
             'temp': temp,
             'temp1': temp1,
             'temp2': temp2,
        }

    return render(request, "ingredients/sozdanie.html", context)


def s(request,slug, slug1, slug2):
    """ Страница ингредиента"""
    product1 = get_object_or_404(Product, slug = slug)
    product2 = get_object_or_404(Product, slug = slug1)
    product3= get_object_or_404(Product, slug=slug2)
    context = {'product1': product1, 'product2': product2, 'product3': product3,}
    return render(request, 'ingredients/s.html', context,)