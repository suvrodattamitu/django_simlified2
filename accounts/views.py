from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	numbers = [1,2,3,4,5,6]
	context = {
		'numbers':numbers,
		'name'	 : 'suvro'
	}
	return render(request,'accounts/home.html',context)