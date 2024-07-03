from django.contrib import admin
from .models import Book, Author, Comment

admin.site.register([Book, Author, Comment])
