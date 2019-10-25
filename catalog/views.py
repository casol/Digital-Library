import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from catalog.models import Book, Author, BookInstance, Genre, Language
from cart.forms import CartAddProductForm

def home(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # Get latest published books
    latest_books = Book.objects.all()[:6]

    # Get list of all genres
    genres = Genre.objects.all()

    # Get list of all authors
    authors = Author.objects.all()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'latest_books': latest_books,
        'genres': genres,
        'authors':authors,
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
    # if slug in url is not correct let Django
    # calculate the canonical URL for an object
    if slug != book.slug:
        return redirect(book.get_absolute_url())

    cart_product_form = CartAddProductForm()
    return render(
        request,
        'catalog/book_detail.html',
        {
            'book': book,
            'cart_product_form':cart_product_form,
        }
    )

def authors(request):
    """Return the list of all authors."""

    author_list = Author.objects.all()
    return render(
        request,
        'catalog/author_list.html',
        {
            'author_list': author_list,
        }
    )


def author_detail(request, pk, slug=None):
    """View function for author details."""

    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()
    
    # if slug in url is not correct let Django   
    # calculate the canonical URL for an object
    if slug != author.slug:
        return redirect(author.get_absolute_url())
    return render(
        request,
        'catalog/author_detail.html',
        {
            'author': author,
            'books': books,
        }
    )
