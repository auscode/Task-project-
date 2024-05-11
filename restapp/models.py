from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128,default='')

class SpamNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)

class Contact(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='contacts')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)