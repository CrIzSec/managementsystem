from django import forms
from .models import Product

class AddTableForm(forms.ModelForm):
    item_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Item Name", "class": "w-full h-full bg-transparent border-0 text-center outline-none"}), label='')
    price = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Price", "class": "w-full h-full bg-transparent text-center border-0 outline-none"}), label='')
    stock = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Stock", "class": "w-full h-full bg-transparent text-center border-0 outline-none"}), label='')

    class Meta:
        model = Product
        fields = ['item_name', 'price', 'stock']