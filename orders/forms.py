from django import forms
from django.forms import TextInput
from .models import Order
from users.models import User


class OrderCreateForm(forms.ModelForm):
    """Customer order form."""
    class Meta:
        model = Order
        exclude = ["user"]
        fields = ['order_first_name', 'order_last_name',
                 'address', 'address2', 'postal_code', 'city',
                 'state', 'phone_number', 'comment']
        labels = {
            'order_first_name': 'First Name',
            'order_last_name': 'Last Name',
            'postal_code': 'Zip'
            }
