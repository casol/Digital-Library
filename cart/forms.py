from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    # the existing quantity has to be updated with the given quantity                                      
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
