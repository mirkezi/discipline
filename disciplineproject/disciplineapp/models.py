from django.db import models

# Create your models here.

class User(models.Model):
    '''model for registered user'''
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        #TODO: need to fix how this is returned in admin page
        return str(self.username)