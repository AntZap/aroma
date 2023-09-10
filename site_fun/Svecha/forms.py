from django import forms

from .models import *

class Sozdanie_svechi(forms.Form):
    aroma = forms.ModelChoiceField(
        queryset=Product.objects.filter(ingredients='1').values_list("name", flat=True).distinct(),
        empty_label=None
    )

    kras = forms.ModelChoiceField(
        queryset=Product.objects.filter(ingredients='2').values_list("name", flat=True).distinct(),
        empty_label=None
    )
    wosk = forms.ModelChoiceField(
        queryset=Product.objects.filter(ingredients='3').values_list("name", flat=True).distinct(),
        empty_label=None
    )

    #GEEKS_CHOICES = Product.objects.all()
    #abs = {}
    #abs ['name'] = GEEKS_CHOICES
    #
    #aroma = forms.CharField(label='Your name', max_length=100)

# res=[]
# res1=tuple(res)
# model= [Ingredients.objects.all()]
# for i in model:
#     res.append(i)