from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish2(request):
    return HttpResponse('<h1>Hello This is From Second Application</h1>')
