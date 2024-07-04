from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import Signup
# Create your views here.

def index(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'index.html', {'users': users})
    else:
        return HttpResponse(status=404)
    
def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user = User(username=username, password=password)
            new_user.save()
    else:
        form = Signup()    
        
    return render(request, 'signup.html', {'form': form})

