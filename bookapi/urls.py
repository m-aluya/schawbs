from django.contrib import admin
from django.urls import path
from bookapi.views import books,book_create

urlpatterns = [
    path('',book_create),
    path('list/', books)
]
