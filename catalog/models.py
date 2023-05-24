from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ManyToManyField('self')
  genre = models.ManyToManyField('self')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  language = models.ManyToManyField('self')