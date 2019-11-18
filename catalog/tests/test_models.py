from datetime import date
import uuid
from django.test import TestCase
from django.template.defaultfilters import slugify


from catalog.models import Author, Book, Genre, Language, BookInstance

class BookModelTest(TestCase):
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
    
    def test_slug_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

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

    def test_subtitle_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('subtitle').max_length
        self.assertEquals(max_length, 200)
    
    def test_publisher_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('publisher').max_length
        self.assertEquals(max_length, 100)
        
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)       
        absolute_url = f'/book/{book.id}/{book.slug}'
        self.assertEqual(book.get_absolute_url(), absolute_url)


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create objects that aren't going to be modified or changed
        # in any of the test methods.
        Author.objects.create(first_name='John', last_name='Rambo',
                             slug=slugify('John Rambo'),
                             date_of_birth=date.fromisoformat('1947-06-06'),
                             date_of_death=date.today())

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
    
    def test_slug_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')
    
    def test_if_death_date_is_greater_then_birth_date(self):
        author = Author.objects.get(id=1)
        self.assertGreater(author.date_of_death, author.date_of_birth)

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
        expected_object_name = f'{author.first_name} {author.last_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        absolute_url = f'/author/{author.id}/{author.slug}'
        self.assertEquals(author.get_absolute_url(), absolute_url)


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(category='Novel', slug=slugify('Novel'))
    
    def test_category_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_slug_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_category_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('category').max_length
        self.assertEquals(max_length, 200)

    def test_slug_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('slug').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = genre.category
        self.assertEqual(str(genre), expected_object_name)


class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        BookInstance.objects.create(id=1, book=book, imprint='Test', price=19, stock=1, status='a')

    def test_imprint_label(self):
        book_instance = BookInstance.objects.get(id=1)
        field_label = book_instance._meta.get_field('imprint').verbose_name
        self.assertEqual(field_label, 'imprint')

    def test_imprint_max_length(self):
        book_instance = BookInstance.objects.get(id=1)
        max_length = book_instance._meta.get_field('imprint').max_length
        self.assertEquals(max_length, 200)

    def test_price_label(self):
        book_instance = BookInstance.objects.get(id=1)
        field_label = book_instance._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_stock_label(self):
        book_instance = BookInstance.objects.get(id=1)
        field_label = book_instance._meta.get_field('stock').verbose_name
        self.assertEqual(field_label, 'stock') 

    def test_status_label(self):
        book_instance = BookInstance.objects.get(id=1)
        field_label = book_instance._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_object_name_is_id_book_title(self):
        book_instance = BookInstance.objects.get(id=1)
        expected_object_name = f'{book_instance.id} ({book_instance.book.title})'
        self.assertEqual(str(book_instance), expected_object_name)

class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='EN')
    
    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
    
    def test_object_name(self):
        language = Language.objects.get(id=1)
        expected_object_name = language.name
        self.assertEqual(str(language), expected_object_name)
