from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrederBook
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, instance=request.user)
        if form.is_valid():
            order = form.save()
            for book in cart:
                OrederBook.objects.create(order=order,
                                          book=book['book'],
                                          price=book['price'],
                                          quantity=book['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart':cart, 'form':form})