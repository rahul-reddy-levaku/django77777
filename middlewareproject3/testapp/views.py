from django.shortcuts import render
from django.http import HttpResponse
def home_page_view(request):
    print(10/0)
    return HttpResponse('<h1>this is from view function</h1>')
