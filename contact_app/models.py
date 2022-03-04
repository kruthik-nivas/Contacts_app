from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PhoneNumbers(models.Model):
    person = models.ForeignKey(Name,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Numbers'

    def __str__(self):
        return self.mobile

class Email(models.Model):
    person = models.ForeignKey(Name,on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email

class Scode(models.Model):
    scode = models.CharField(max_length=10)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return Scode