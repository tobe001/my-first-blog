from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cv(request):
	return HttpResponse("<html><title>My CV</title></html>")