from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# the class Book is in fact he database book
class Book(models.Model):
    title = models.CharField(max_length= 50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100) #null=True means that the entry in the DB will receive a null value if no value is provided
    is_bestselling = models.BooleanField(default=False) # by default the book is not best selling

    def __str__(self):
        return f"{self.title})  ({self.rating})"
    