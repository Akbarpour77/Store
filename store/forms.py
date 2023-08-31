from django import forms
from .models import Mobiles


class Product_list(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = '__all__'
