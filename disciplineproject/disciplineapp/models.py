from django.db import models

# Create your models here.

class User(models.Model):
    '''model for registered user'''
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Username: {User.username}, Password: {User.password}., Active: {User.is_active}"