from django.db import models

class authors(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(authors, on_delete=models.CASCADE) 
    price = models.FloatField()
    book_cover = models.TextField()
    apublished_date = models.DateField()
    number_of_copies = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.title