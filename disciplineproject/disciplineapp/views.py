from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404)
    
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_request(request):
    logout(request)
    return redirect('/')