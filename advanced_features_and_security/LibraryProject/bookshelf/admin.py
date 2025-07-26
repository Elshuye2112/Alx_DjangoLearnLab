from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ["username", "email", "first_name", "last_name", "is_staff", "date_of_birth"]
    search_fields = ["username", "email", "first_name", "last_name"]

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year',)  # Filters on the right sidebar
    search_fields = ('title', 'author')  # Search box for title and author

# Alternative registration without decorator:
# admin.site.register(Book, BookAdmin)
