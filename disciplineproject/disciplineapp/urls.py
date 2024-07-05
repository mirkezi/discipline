from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('signup', view=views.signup, name='signup'),
    path('login/', view=views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]