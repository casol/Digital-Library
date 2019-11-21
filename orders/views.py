from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrderBook, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import User
from .tasks import order_created


@login_required
def order_create(request):
    """Render the form and create a new order."""

    cart = Cart(request)
    # get logged user and declare the initial values
    user = User.objects.get(email=request.user)
    data = {'order_first_name': user.first_name,
            'order_last_name': user.last_name}
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, initial=data)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order = form.save()
            for book in cart:
                OrderBook.objects.create(order=order,
                                         book=book['book'],
                                         price=book['price'],
                                         quantity=book['quantity'])
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id, user.email)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm(initial=data)
    return render(request, 'orders/order/create.html',
                  {'cart':cart, 'form':form})

@login_required
def user_orders(request):
    """Render orders for the current user."""

    user_order = Order.objects.filter(user=User.objects.get(email=request.user))
    #user_order.order_set.all()
    return render(
                request,
                'orders/created.html',
                {
                    'user_order': user_order
                }
            )
