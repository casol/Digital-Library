import re
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from catalog.models import Book, Author, BookInstance, Genre, Language


def home(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/home.html', context=context)

def books(request):
    """Return the list of all books."""

    # Get list of all books
    book_list = Book.objects.all()
    return render(
        request,
        'catalog/book_list.html',
        {
            'book_list': book_list,
        }
    )

def book_detail(request, pk, slug=None):
    """View function for details of the specific book."""
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
        'catalog/book_detail.html',
        {
            'book': book,
        }
    )
