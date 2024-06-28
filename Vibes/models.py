from django.db import models

class Destination(models.Model):

    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    image = models.ImageField(upload_to='img')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
