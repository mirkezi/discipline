'''Definition of Forms that will be implemented on website'''
from django.contrib.auth.forms import UserCreationForm
from django.apps import apps

User = apps.get_model('auth', 'User')

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']