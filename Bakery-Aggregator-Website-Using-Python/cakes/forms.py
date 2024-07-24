# cakes/forms.py

from django import forms
from .models import Cake, Order

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'  # Include all fields from the Cake model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs['class'] = 'form-control'  # Add CSS class for styling

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address']