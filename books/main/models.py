from django.db import models

class Books(models.Model):
    title=models.CharField('Book name', max_length=100)
    subtitle=models.CharField('Short description', max_length=100)
    description=models.TextField('About book')

    price=models.CharField('Book price', max_length=100)
    genre=models.CharField('Genre', max_length=20)
    author=models.CharField('Author', max_length=20)

    year=models.CharField('Date of issue', max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.title