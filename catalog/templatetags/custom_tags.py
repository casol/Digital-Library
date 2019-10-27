from django import template
from catalog.models import Book, Genre


register = template.Library()

@register.inclusion_tag('catalog/book_list.html')
def sidebar():
    """Custom tag for the sidebar content."""
    genres1 = Genre.objects.all()
    return {'genres1': genres1}
