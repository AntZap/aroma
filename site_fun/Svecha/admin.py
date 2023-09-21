from django.contrib import admin
from .models import Ingredients, Product

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ingredients, IngredientsAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['ingredients', 'name', 'slug', 'description', 'primechanie', 'updated']
    list_filter = ['updated']
    #list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
# Register your models here.
