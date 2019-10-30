from django import template
from catalog.models import Book, Genre, Author


register = template.Library()

@register.inclusion_tag('catalog/sidebar.html')
def sidebar():
    """Custom tag for the sidebar content."""
    # Get list of all genres
    genres = Genre.objects.all()
    # Get list of all authors
    authors = Author.objects.all()
    return {'genres': genres,
            'authors':authors}
