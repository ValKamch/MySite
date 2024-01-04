from django import forms
#from django.core import validators

from .models import Product

#class ProductForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    price = forms.DecimalField(min_value=1, max_value=100000, label="Цена продукта", decimal_places=2)
#    description = forms.CharField(label="Product description",
#                                   widget=forms.Textarea(attrs={"rows":5}),
#                                   validators=[validators.RegexValidator(
#                                       regex=r"great",
#                                       message="Должно быть определенное слово"
#                                   )
#                                   ]
#                                )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"
  
