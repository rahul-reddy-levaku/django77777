from django.shortcuts import render
from django.http import HttpResponse
def welcome_view(request):
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
