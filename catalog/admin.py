from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language


admin.site.register(Language)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"slug": ('category',)}

class BooksInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BooksInline]
    # Set prepopulated_fields to a dictionary mapping field
    # names to the fields it should prepopulate from:
    prepopulated_fields = {"slug": ("first_name", "last_name")}

# The admin interface has the ability to edit models on the same page
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_authors', 'display_genre')
    inlines = [BooksInstanceInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'price', 'created')
    list_display = ('book', 'status', 'stock', 'price', 'id')
    #readonly_fields = ('created', )
    # Set fieldsets to control the layout of admin
    fieldsets = (
        (None, {
            'fields': ('book', 'stock', 'price', 'imprint',
            'id',)
        }),
        ('Availability', {
            'fields': ('status',)
        }),
    )
