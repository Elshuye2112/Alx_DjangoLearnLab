# Django Admin Setup for Book Model

- Registered `Book` model in `bookshelf/admin.py` using `BookAdmin`.
- Configured `list_display` to show `title`, `author`, `publication_year`.
- Added `list_filter` on `publication_year`.
- Enabled `search_fields` on `title` and `author`.
- Access admin at `http://127.0.0.1:8000/admin/`.
- Created superuser via `python manage.py createsuperuser`.
