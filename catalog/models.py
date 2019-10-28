import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Book(models.Model):
    """Book."""

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
    cover = models.ImageField(upload_to='book_covers/%Y/%m/', default='book_covers/None/no-img.jpg',
                              blank=True)
    slug = models.SlugField(help_text='A slug is a short label, used in URLs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.category for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def display_authors(self):
        return ', '.join(author.last_name for author in self.authors.all())   

    display_genre.short_description = 'Authors'

    def get_absolute_url(self):
        return reverse('catalog:book_detail', args=[str(self.id), self.slug])

    def __str__(self):
        return self.title


class Author(models.Model):
    """Model representing a book author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    slug = models.SlugField(blank=False, null=True,
                            help_text='A slug is a short label, used in URLs')

    # Overide a save method to update slug for all future records
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.first_name, self.last_name)
    #     super(Author, self).save(*args, **kwargs)
    # To generate a slug in existing table
    # >>> from django.template.defaultfilters import slugify
    # >>> for obj in MyModel.objects.all():
    # ...     obj.slug = slugify(obj.title)
    # ...     obj.save()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('catalog:author_detail', args=[str(self.id), self.slug])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#class Isbn(model.Model):
class Genre(models.Model):
    """Model representing a book genre."""
    category = models.CharField(max_length=200, help_text='Enter a book genre')
    slug = models.SlugField(max_length=200, help_text='A slug is a short label, used in URLs')
    
    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class BookInstance(models.Model):
    """Model representing a specific copy of a book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole store')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    AVAILABILITY_STATUS = (
        ('u', 'Unavailable'),
        ('c', 'Coming soon'),
        ('a', 'Available'),
        ('s', 'Sold out'),
    )

    status = models.CharField(
        max_length=1,
        choices=AVAILABILITY_STATUS,
        blank=True,
        default='u',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['book']

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
