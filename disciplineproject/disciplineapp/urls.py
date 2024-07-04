from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('signup', view=views.signup, name='signup'),
]