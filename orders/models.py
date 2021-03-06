from django.db import models

from users.models import User
from catalog.models import Book


class Order(models.Model):
    """Model representing a customer detail information."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    braintree_id = models.CharField(max_length=150, blank=True)
    order_first_name = models.CharField(max_length=100)
    order_last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=16)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    comment = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        """
        Get total cost for all the books in the order.
        OrderBook.objects.all()
        """
        return sum(book.get_cost() for book in self.books.all())

class OrderBook(models.Model):
    """Model allows to store the book and quantity with price."""

    order = models.ForeignKey(Order, related_name='books',
                              on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='order_book',
                             on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
   
    def get_cost(self):
        return self.price * self.quantity
