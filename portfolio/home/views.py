from django.shortcuts import render
from django.http import HttpResponse

def home(request, template="home/home.html"):
	number = 1
	context = {
		'number': number,
	}
	return render(request,template,context)

def blog(request):

	return HttpResponse("on blog")
