from django.urls import path
from . import views

app_name = 'Svecha'

urlpatterns = [
    #"""Домашняя страница"""
    path('', views.index, name='home'),
    #"""Страница по категориям"""
    path('sostavlyushie', views.product_list, name='product_list'),
    #"""Страница с перечнем всех составляющих свечи согласно выбранной категории"""
    path('<slug:category_slug>/', views.Ingredient_list, name='Ingredient_list'),
    #""прописанное условие в файле list передает id  и англ название, а после этого показывает информацию о нужном составляющем"""
    #"""Страница с описанием выбранного составляющего свечи согласно категориям"""
    path('<int:id>/<slug:slug>/', views.product_detail, name='ingredients_detail'),
    #"""" Страница с формой где мы выбираем составляющие свечи, а затем получаем свечу с описание ингредиентов"""
    path('sozdanie', views.sozdanie, name='sozdanie'),
    #""""  получаем свечу с описание, выбранных ингредиентов"""
    path('<slug:slug>/<slug:slug1>/<slug:slug2>/', views.res_svecha, name='res_svecha'),
]
