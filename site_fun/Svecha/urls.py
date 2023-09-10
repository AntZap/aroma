from django.urls import path
from . import views

app_name = 'Svecha'

urlpatterns = [
    #"""Домашняя страница"""
    path('', views.product_list, name='product_list'),
    #"""Страница по категориям"""
    path('<slug:category_slug>/', views.ing, name='sostav'),
    #""прописанное условие в файле list передает id  и англ название, а после этого показывает информацию о нужном составляющем"""
    path('<int:id>/<slug:slug>/', views.product_detail, name='ingredients_detail'),

    path('sozdanie', views.sozdanie, name='game'),

    path('<slug:slug>/<slug:slug1>/<slug:slug2>/', views.s, name='s'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='ingredients_detail'),
]


# def sozdanie(request):
#     submitbutton = request.POST.get("Submit")
#     products = Product.objects.all()
#     location_list = Sozdanie_svechi(request.POST or None)
#     temp = ""
#     temp1 = ""
#     temp2 = ""
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
#
#         }
#
#     return render(request, "ingredients/sozdanie.html", context)