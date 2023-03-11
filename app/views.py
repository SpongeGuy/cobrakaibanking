from django.shortcuts import  render #redirect
#from django.contrib.auth import login
#from django.contrib import messages


def home(request):
	return render(request, 'app/index.html' )

def accounts(request):
	return render(request, 'app/accounts.html')

def planning(request):
	return render(request, 'app/planning.html')

def service(request):
	return render(request, 'app/service.html')

def login(request):
	return render(request, 'app/login.html')