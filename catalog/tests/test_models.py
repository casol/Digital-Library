from datetime import date
from django.test import TestCase

from catalog.models import Author, Book, Genre, Language

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup a book with related """
        author = Author.objects.create(first_name='John', last_name='Rambo')        
        genre = Genre.objects.create(category='Novel')
        Language.objects.create(name='English')        
        language = Language.objects.get(id=1)
        book = Book.objects.create(title='TestBook',
        subtitle='The best book for testing', publisher='BookPrint',
        description='TestTestTest', published_date=date.today(),
        isbn='978-1541392304', pages=233, language=language)
        book.authors.add(author)
        book.genre.add(genre)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_authors_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')
    
    def test_subtile_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('subtitle').verbose_name
        self.assertEqual(field_label, 'subtitle')
    
    def test_publisher_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('publisher').verbose_name
        self.assertEqual(field_label, 'publisher')
    
    def test_description_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    def test_published_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('published_date').verbose_name
        self.assertEqual(field_label, 'published date') 

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_pages_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('pages').verbose_name
        self.assertEqual(field_label, 'pages')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create objects that aren't going to be modified or changed
        # in any of the test methods.
        Author.objects.create(first_name='John', last_name='Rambo')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')
    
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')
    
    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(), '/catalog/author/1')