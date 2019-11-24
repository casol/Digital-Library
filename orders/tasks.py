from celery import task
from django.core.mail import send_mail
from .models import Order, OrderBook


@task
def order_created(order_id, user_email):
    """
    Send an email notification when an order
    has been successfully created.
    """
    order = Order.objects.get(id=order_id)
    book_order = OrderBook.objects.filter(order=order_id)
    books = ''
    for book in book_order:
        books += f'{book.book}, {book.quantity} x {book.price} USD \n'
    subject = f'Digital BookStore - order nr. {order.id}'
    message = f'Hello {order.order_first_name},\n\nYou just have successfully placed an order.\n Find\
    your order details below \n {books} \nShipping details: '
    mail_sent = send_mail(subject,
                          message,
                          'notification@digitalbookstore.com',
                          [user_email])
    return mail_sent
