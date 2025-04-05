from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import auth

# Create your views here.

def home(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      print(f"hello {request.user.username}")
      return render(request, '')

def user_register(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      return redirect('/')
  else:
    form = CustomUserCreationForm()

  return render(request, 'accounts/register.html', {'form':form})

def user_login(request):
  #Create form for password and that and return home after logging in
  firstAttempt = True
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user:
      auth.login(request, user)
      return redirect('/')
    else:
      firstAttempt = False
      
  return render(request,'accounts/login.html',{'firstAttempt':firstAttempt})

def user_logout(request):
    auth.logout(request)
    return redirect('/')
