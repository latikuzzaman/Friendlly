from django.db import models

# Create your models here.


class userinfo(models.Model):
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=gender, max_length=15, default='Choose')
