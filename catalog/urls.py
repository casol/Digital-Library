from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    # two url patterns poiting to one view.
    path('book/<int:pk>', views.book_detail, name='book_detail'),
    path('book/<int:pk>/<slug:slug>/', views.book_detail, name='book_detail')
]
