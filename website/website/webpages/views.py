from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})

def jungle_view(request, *args, **kwargs):
	return render(request, "jungle.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def main_view(request, *args, **kwargs):
	return render(request, "main.html", {})
