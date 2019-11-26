from datetime import date
import uuid
import random
from django.test import TestCase
from django.template.defaultfilters import slugify

from users.models import User, UserManager
from catalog.models import Author, Book, Genre, Language, BookInstance
from orders.models import Order, OrderBook


class OrderTestClass(TestCase):
    """Test order model."""

    @classmethod
    def setUpTestData(cls):
        """Set order and user object for testing."""
        user = User.objects._create_user(email='test@test.com', first_name='Test',
                                         last_name='TestLastName', password='testpasswd')
        order = Order.objects.create(user=user, order_first_name=user.first_name, order_last_name=user.last_name, address='Test Street 12/32',
                                     address2='test/test 12&1";', postal_code='9210', city='Test City', state="TestState",
                                     comment='test', phone_number='648234181', paid=False)
        
    def test_user_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_order_first_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_first_name').verbose_name
        self.assertEqual(field_label, 'order first name')
    
    def test_order_last_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_last_name').verbose_name
        self.assertEqual(field_label, 'order last name')
    
    def test_address_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_address2_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('address2').verbose_name
        self.assertEqual(field_label, 'address2')

    def test_postal_code_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('postal_code').verbose_name
        self.assertEqual(field_label, 'postal code')
    
    def test_city_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_state_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_comment_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('comment').verbose_name
        self.assertEqual(field_label, 'comment')

    def test_phone_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_paid_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('paid').verbose_name
        self.assertEqual(field_label, 'paid')

    def test_order_first_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_first_name').max_length
        self.assertEquals(max_length, 100)

    def test_order_last_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_last_name').max_length
        self.assertEquals(max_length, 100)

    def test_address_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('address').max_length
        self.assertEquals(max_length, 150)

    def test_address2_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('address2').max_length
        self.assertEquals(max_length, 150)

    def test_postal_code_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('postal_code').max_length
        self.assertEquals(max_length, 16)

    def test_city_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('city').max_length
        self.assertEquals(max_length, 100)

    def test_state_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('state').max_length
        self.assertEquals(max_length, 100)

    def test_comment_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('comment').max_length
        self.assertEquals(max_length, 250)

    def test_phone_number_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 12)
    
    def test_object_name_is_order_id(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'Order {order.id}'
        self.assertEqual(expected_object_name, str(order))


class OrderBookTestClass(TestCase):
    """Test book order model."""

    @classmethod
    def setUpTestData(cls):
        """Set book, user, order for book order testing."""

        user = User.objects._create_user(email='test@test.com', first_name='Test',
                                         last_name='TestLastName', password='testpasswd')
        order = Order.objects.create(user=user, order_first_name=user.first_name, order_last_name=user.last_name, address='Test Street 12/32',
                                     address2='test/test 12&1";', postal_code='9210', city='Test City', state="TestState",
                                     comment='test', phone_number='648234181', paid=False)
        # Set up book for testing
        author = Author.objects.create(first_name='John', last_name='Rambo')
        genre = Genre.objects.create(category='Novel')
        Language.objects.create(name='English')
        language = Language.objects.get(id=1)
        # Create 4 book objects
        for book_id in range(1, 5):
            book = Book.objects.create(title=f'TestBook{book_id}', subtitle=f'The best book for testing{book_id}',
                publisher=f'BookPrint{book_id}', description=f'{book_id}TestTestTest',
                published_date=date.today(), isbn=f'978-15413923{book_id}',
                pages=233, language=language, slug=slugify(f'TestBook{book_id}'))
            book.authors.add(author)
            book.genre.add(genre)
        # Add books to the order
        for book_object in Book.objects.all():
            OrderBook.objects.create(order=order, book=book_object, price=float(random.randint(1000, 2000))/100, quantity=random.randint(1, 4))
    
    def test_order_label(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        field_label = order_book_instance._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order')
    
    def test_book_label(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        field_label = order_book_instance._meta.get_field('book').verbose_name
        self.assertEqual(field_label, 'book')

    def test_price_label(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        field_label = order_book_instance._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_quantity_label(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        field_label = order_book_instance._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_price_max_digits(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        max_digits = order_book_instance._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 10)

    def test_object_name_is_order_book_id(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        expected_object_name = f'{order_book_instance.id}'
        self.assertEqual(expected_object_name, str(order_book_instance))

    def test_get_cost(self):
        order_book_instance = OrderBook.objects.filter(order=1).first()
        expected_cost = order_book_instance.price * order_book_instance.quantity
        self.assertEqual(expected_cost, order_book_instance.get_cost())
