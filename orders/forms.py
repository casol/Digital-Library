from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Customer order form."""
    class Meta:
        model = Order
        fields = ['user', 'address', 'postal_code', 'city', 'state',
                 'phone_number', 'comment']
