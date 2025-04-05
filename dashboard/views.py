from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

  return render(request, 'dashboard/home.html', {'user':request.user})


