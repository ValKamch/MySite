from django.contrib.auth.models import Group
from django.forms import ModelForm, ImageField, ClearableFileInput, Form, FileField

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

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    image = ImageField(
        widget=ClearableFileInput(attrs={"multiple": True})
    )
  

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "name",

class CSVImportForm(Form):
    csv_file = FileField()
