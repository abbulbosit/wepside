from django.shortcuts import render

from .models import Book


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def book(request):
    books = Book.objects.all()
    context = {'all_books': books}
    return render(request, 'books.html', context=context)
