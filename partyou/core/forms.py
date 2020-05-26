from django import forms

from partyou.core.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control'}),
                   }
