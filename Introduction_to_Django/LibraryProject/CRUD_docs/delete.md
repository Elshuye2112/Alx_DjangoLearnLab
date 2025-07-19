
---

### delete.md

```markdown
# Delete Operation

```python
book = Book.objects.first()
book.delete()
print(Book.objects.all())
# Output:
# <QuerySet []>
