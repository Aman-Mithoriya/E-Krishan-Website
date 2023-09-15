from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    emailId=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=10)
    textholder=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self):
            return self.emailId