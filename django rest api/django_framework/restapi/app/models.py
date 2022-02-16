from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_mumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    date= models.DateField()

    def __str__(self):
        return self.name