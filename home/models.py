from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    query=models.CharField(max_length=122)
    date=models.CharField(max_length=30)
    def __str__(self):
        return self.name
        #return self.name+ " _ " + self.email
