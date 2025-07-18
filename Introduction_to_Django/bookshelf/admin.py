from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year',)  # Filters on the right sidebar
    search_fields = ('title', 'author')  # Search box for title and author

# Alternative registration without decorator:
# admin.site.register(Book, BookAdmin)
