
---

### update.md

```markdown
# Update Operation

```python
book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output:
# Nineteen Eighty-Four
