from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Books)
class booksAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'date',
    )
    list_display = (
        'id',
        'book_name',
        'author',
        'book_count',
    )


@admin.register(BorrowBook)
class BorrowbooksAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'date',
    )
    list_display = (
        'id',
        'book',
        'quantity',
        'date'
    )
