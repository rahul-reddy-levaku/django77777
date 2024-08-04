from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    s='<h1>Hello students welcome to Mahesh sir django classes</h1>'
    return HttpResponse(s)
