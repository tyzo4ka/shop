from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='name')
    description = forms.CharField(max_length=3000, required=True, label="Description")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label='Category')
    remainder = forms.IntegerField(min_value=1, required=True, label="Amount")
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Price")

