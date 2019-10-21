from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Book, BookInstance
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book_instance=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
