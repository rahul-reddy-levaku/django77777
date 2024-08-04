from django.shortcuts import render
from django.http import HttpResponse

def hydviews(request):
    s = '<h1>Hyderabad jobs information</h1>'
    return HttpResponse(s)

def bang_views(request):
    s = '<h1>bangalore jobs information</h1>'
    return HttpResponse(s)

def pune_jobs(request):
    s = '<h1>Pune jobs information</h1>'
    return HttpResponse(s)

def bihar_jobs(request):
    s = '<h1>bihar jobs information</h1>'
    return HttpResponse(s)

