from django.contrib import admin
from .models import Ingredients, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ingredients, IngredientsAdmin)

class ProductResource(resources.ModelResource):

    class Meta:
        model = Product

class ProductAdmin(ImportExportModelAdmin):
    list_display = ['ingredients', 'name', 'slug', 'description', 'primechanie', 'updated']
    list_filter = ['ingredients']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
# Register your models here.



