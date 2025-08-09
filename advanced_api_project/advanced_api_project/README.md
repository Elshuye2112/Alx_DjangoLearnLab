# Advanced API Project – Book API

## Endpoints
- **GET** `/api/books/` – List all books (public)
- **GET** `/api/books/<id>/` – Retrieve a book (public)
- **POST** `/api/books/create/` – Create a book (authenticated only)
- **PUT** `/api/books/<id>/update/` – Update a book (authenticated only)
- **DELETE** `/api/books/<id>/delete/` – Delete a book (authenticated only)

## Permissions
- Public can view books.
- Only authenticated users can create, update, and delete.
- Validation ensures ISBN is numeric.
