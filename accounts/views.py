from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def home(request):
	numbers = [1,2,3,4,5,6]
	context = {
		'numbers':numbers,
		'name'	 : 'suvro'
	}
	return render(request,'accounts/home.html',context)


def register(request):
	if request.method == 'GET':
		form = RegistrationForm()
		context = {
			'form' : form
		}
		return render(request,'accounts/register.html',context)
	else:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')

def profile(request):
	context = {
		'user':request.user
	}
	return render(request,'accounts/profile.html',context)

def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('view_profile')

	else:
		form = UserChangeForm(instance=request.user)
		context = {
			'form' : form
		}
		return render(request,'accounts/edit_profile.html',context)



