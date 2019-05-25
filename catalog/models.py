from django.db import models
from django.urls import reverse
import uuid

class Book(models.Model): 
    title = models.CharField(max_length=200, blank=False)
    authors = models.ManyToManyField('Author')
    subtitle = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000,                                    
                                   help_text='Enter a brief description of the book')
    published_date = models.DateField(null=True, blank=True)
    # https://en.wikipedia.org/wiki/International_Standard_Book_Number
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField('Genre', help_text='Choose a book genre')
    pages = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.category for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def display_authors(self):
        return ', '.join(author.last_name for author in self.authors.all())        

    display_genre.short_description = 'Authors'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title   


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

#class Isbn(model.Model):
class Genre(models.Model):
    category = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.category


class BookInstance(models.Model):
    """Model representing a specific copy of a book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
