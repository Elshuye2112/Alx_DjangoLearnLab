from django.contrib import admin
<<<<<<< HEAD
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year',)  # Filters on the right sidebar
    search_fields = ('title', 'author')  # Search box for title and author

# Alternative registration without decorator:
# admin.site.register(Book, BookAdmin)
=======

# Register your models here.
>>>>>>> 08a2d9d (Add bookshelf app with Book model and documented CRUD operations)
