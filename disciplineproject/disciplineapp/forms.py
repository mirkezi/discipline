'''Definition of Forms that will be implemented on website'''
from django import forms

class Signup(forms.Form):
    '''define the signup form '''
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
