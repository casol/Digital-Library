from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id, user_email):
    """
    Send an email notification when an order
    has been successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Digital BookStore - order nr. {order.id}'
    message = f'Hello {order.order_first_name},\n\nYou just have successfully placed an order.\n Find your order details below \
    gfhuj'
    mail_sent = send_mail(subject,
                          message,
                          'notification@digitalbookstorec.com',
                          [user_email])
    return mail_sent
