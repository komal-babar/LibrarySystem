from django.db import models

# Create your models here.
class BookData(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    

   