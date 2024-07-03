from django.urls import path
from .views import home, login, register, book

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('book/', book, name='book'),
]
