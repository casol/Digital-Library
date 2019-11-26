from django.test import TestCase

from orders.models import Order, OrderBook
from orders.forms import OrderCreateForm


class OrderCreateFormTest(TestCase):
    """Test order deatails form."""
    
    def test_order_form_order_first_name_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['order_first_name'].label == 'First Name')
    
    def test_order_form_order_last_name_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['order_last_name'].label == 'Last Name')

    def test_order_form_address_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['address'].label == 'Address')

    def test_order_form_address2_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['address2'].label == 'Address2')

    def test_order_form_city_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['city'].label == 'City')

    def test_order_form_state_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['state'].label == 'State')

    def test_order_form_phone_number_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['phone_number'].label == 'Phone number')

    def test_order_form_comment_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['comment'].label == 'Comment')

    def test_order_form_postal_code_label(self):
        form = OrderCreateForm()
        self.assertTrue(form.fields['postal_code'].label == 'Zip')

    def test_order_from_excluded_field(self):
        form = OrderCreateForm()
        # self.assertRaise() takes a callable <- lambda
        self.assertRaises(KeyError, lambda: form.fields['user'])
