from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    # Lookup by id only, use slug only for SEO/readability
    path('book/<int:pk>', views.book_detail, name='book_detail'),
    path('book/<int:pk>/<slug:slug>/', views.book_detail, name='book_detail'),
    path('author/<int:pk>', views.author_detail, name='author_detail'),
    path('author/<int:pk>/<slug:slug>', views.author_detail, name='author_detail')
]
