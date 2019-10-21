from decimal import Decimal
from django.conf import settings
from catalog.models import Book, BookInstance


class Cart(object):
    """Cart class allow manage the shopping cart."""

    def __init__(self, request):
        """Initialize the cart."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in a session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, book_instance, quantity=1, update_quantity=False):
        """Add a book to the cart or update quantity"""

        # convert id to string - session data use JSON
        book_instance_id = str(book_instance.id)
        if book_instance_id not in self.cart:
            self.cart[book_instance_id] = {'quantity':0,
                                           'price': str(book_instance.price)}
        if update_quantity:
            self.cart[book_instance_id]['quantity'] = quantity
        else:
            self.cart[book_instance_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Save modified session """
        self.session.modified = True
                            
    def remove(self, book_instance):
        """Remove a book instance from the cart."""
        book_instance_id = str(book_instance.id)
        if book_instance_id in self.cart:
            del self.cart[book_instance_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the books in the cart and get
        the book from the database.
        """
        book_instance_ids = self.cart.keys()
        # get book objects and add to the cart
        books = BookInstance.objects.filter(id__in=book_instance_ids)
        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book
        # cart = {'book_id':{'price':11, 'quantity':3}}
        # cart.values() >>> {'price':11, 'quantity':3}
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Count the total price of the cart."""
        return sum(Decimal(item['price']) * item['quantity'] for item in
        self.cart.values())

    def clear(self):
        """Remove cart from session."""
        del self.session[settings.CART_SESSION_ID]
        self.save()
