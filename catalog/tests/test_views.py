from django.test import TestCase
from django.urls import reverse
from datetime import date
from django.template.defaultfilters import slugify

from catalog.views import *


class HomeViewTest(TestCase):
    """Test home view."""

    @classmethod
    def setUpTestData(cls):
        pass
        #
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/home.html')


class BooksViewTest(TestCase):
    """Test books view."""
 
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='John', last_name='Rambo')
        genre = Genre.objects.create(category='Novel')
        Language.objects.create(name='English')
        language = Language.objects.get(id=1)
        for book_id in range(1, 11):
            book = Book.objects.create(title=f'TestBook{book_id}', subtitle=f'The best book for testing{book_id}',
                publisher=f'BookPrint{book_id}', description=f'{book_id}TestTestTest',
                published_date=date.today(), isbn=f'978-15413923{book_id}',
                pages=233, language=language, slug=slugify(f'TestBook{book_id}'))
            book.authors.add(author)
            book.genre.add(genre)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog:books'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('catalog:books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_list.html')

    def test_view_lists_all_books(self):
        # Get list of all books
        response = self.client.get(reverse('catalog:books'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['book_list']) == 10)

class BookDetailViewTest(TestCase):
    """Test book detail view."""

    @classmethod
    def setUpTestData(cls):
        """Setup a book with related objects."""
        author = Author.objects.create(first_name='John', last_name='Rambo')
        genre = Genre.objects.create(category='Novel')
        Language.objects.create(name='English')
        language = Language.objects.get(id=1)
        book = Book.objects.create(title='TestBook',
                                  subtitle='The best book for testing', publisher='BookPrint',
                                  description='TestTestTest', published_date=date.today(),
                                  isbn='978-1541392304', pages=233, language=language, slug=slugify('TestBook'))
        book.authors.add(author)
        book.genre.add(genre)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        book = Book.objects.get(id=1)
        response = self.client.get(reverse('catalog:book_detail', args=[str(book.id), book.slug]))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_id_only(self):
        # if slug in url is not correct let Django
        # calculate the canonical URL for an object
        book = Book.objects.get(id=1)
        response = self.client.get(reverse('catalog:book_detail', args=[str(book.id)]))
        # expect http redirect code 302
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_incorrect_slug(self):
        # if slug in url is not correct let Django
        # calculate the canonical URL for an object
        book = Book.objects.get(id=1)
        response = self.client.get(reverse('catalog:book_detail', args=[str(book.id), 'incorrect_slug']))
        # expect http redirect code 302
        self.assertEqual(response.status_code, 302)
    
    def test_view_uses_correct_template(self):
        book = Book.objects.get(id=1)
        response = self.client.get(reverse('catalog:book_detail', args=[str(book.id), book.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_detail.html')
    
    def test_view_if_list_a_book(self):
        book = Book.objects.get(id=1)
        response = response = self.client.get(reverse('catalog:book_detail', args=[str(book.id), book.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['book'] == book)


class AuthorsViewTest(TestCase):
    """Test author view."""
 
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='John', last_name='Rambo')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_view_lists_all_books(self):
        # Get list of all books
        response = self.client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['author_list']) == 1)


class AuthorDetailViewTest(TestCase):
    """Test author detail view."""

    @classmethod
    def setUpTestData(cls):
        """Setup a book with related objects."""
        author = Author.objects.create(first_name='John', last_name='Rambo', slug=slugify('John Rambo'))
        genre = Genre.objects.create(category='Novel')
        Language.objects.create(name='English')
        language = Language.objects.get(id=1)
        book = Book.objects.create(title='TestBook',
                                  subtitle='The best book for testing', publisher='BookPrint',
                                  description='TestTestTest', published_date=date.today(),
                                  isbn='978-1541392304', pages=233, language=language, slug=slugify('TestBook'))
        book.authors.add(author)
        book.genre.add(genre)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('catalog:author_detail', args=[str(author.id), author.slug]))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_id_only(self):
        # if slug in url is not correct let Django
        # calculate the canonical URL for an object
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('catalog:author_detail', args=[str(author.id)]))
        # expect http redirect code 302
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_incorrect_slug(self):
        # if slug in url is not correct let Django
        # calculate the canonical URL for an object
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('catalog:author_detail', args=[str(author.id), 'incorrect_slug']))
        # expect http redirect code 302
        self.assertEqual(response.status_code, 302)
    
    def test_view_uses_correct_template(self):
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('catalog:author_detail', args=[str(author.id), author.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_detail.html')
    
    def test_view_if_list_a_book(self):
        author = Author.objects.get(id=1)
        response = response = self.client.get(reverse('catalog:author_detail', args=[str(author.id), author.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['author'] == author)
    
    def test_view_books_associated_with_author(self):
        author = Author.objects.get(id=1)
        # query set
        books_author = author.book_set.all()    
        response = response = self.client.get(reverse('catalog:author_detail', args=[str(author.id), author.slug]))        
        self.assertTrue(response.context['author_books'] == books_author)
