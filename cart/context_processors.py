from .cart import Cart

def cart(request):
    """
    The context_processors takes a request object as their argument
    and return a dictionary of items to be merged into the context.
    """
    return {'cart': Cart(request)}
