from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path("hello/<name>", views.hello_there, name="hello_there"),
]
