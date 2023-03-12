from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
	return render(request, 'app/index.html' )

def accounts(request):
	return render(request, 'app/accounts.html')

def planning(request):
	return render(request, 'app/planning.html')

def service(request):
	return render(request, 'app/service.html')

def login(request):
	return render(request, 'django.contrib.auth.urls')

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("app:home")
		messages.error(request, "Unsuccessful registration, Invalid information.")
	form = NewUserForm()
	return render (request, 'app/register.html', context={'register_form':form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("app:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="app/index.html", context={"login_form":form})