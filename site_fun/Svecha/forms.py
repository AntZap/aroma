from django import forms
from django.forms import RadioSelect
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
    class Meta:
        fields = ["aroma", "kras", "wosk"]

        widgets = {
        "aroma": RadioSelect(attrs={'class': 'form-control'}),
        "kras": RadioSelect(attrs={'class': 'form-control'}),
        "wosk": RadioSelect(attrs={'class': 'form-control'}),

        }
