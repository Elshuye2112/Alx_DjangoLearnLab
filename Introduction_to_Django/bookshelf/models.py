from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
<<<<<<< HEAD
<<<<<<< HEAD
        return self.title
=======
        return f"{self.title} by {self.author} ({self.publication_year})"
>>>>>>> 08a2d9d (Add bookshelf app with Book model and documented CRUD operations)
=======
        return self.title
>>>>>>> f0e9327 (Complete bookshelf app with Book model, CRUD docs, and admin setup)
