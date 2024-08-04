from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    s = '<h1>Hello students welcome to Mahesh sir django classes</h1>'
    return HttpResponse(s)