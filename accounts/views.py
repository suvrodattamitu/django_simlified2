from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



def home(request):
	numbers = [1,2,3,4,5,6]
	context = {
		'numbers':numbers,
		'name'	 : 'suvro'
	}
	return render(request,'accounts/home.html',context)


def register(request):
	if request.method == 'GET':
		form = UserCreationForm()
		context = {
			'form' : form
		}
		return render(request,'accounts/register.html',context)
	else:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
