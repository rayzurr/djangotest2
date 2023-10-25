from django.shortcuts import render

from django.http import HttpResponse
# Create your views
 
def index(response):
 	return HttpResponse("<h1>tech with $name Raymond!</h1>")

def v1(response):
 	return HttpResponse("<h2>view one</h1>")