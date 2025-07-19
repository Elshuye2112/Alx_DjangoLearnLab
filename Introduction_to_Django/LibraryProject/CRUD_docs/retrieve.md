
---

### retrieve.md

```markdown
# Retrieve Operation

```python
book = Book.objects.first()
print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949
