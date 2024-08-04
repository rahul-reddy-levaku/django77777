import datetime

from django.shortcuts import render
from django.http import HttpResponse

def time_info(request):
    date = datetime.datetime.now()
    msg = '<h1>Hello friend very'
    h = int(date.strftime('%H'))
    if h<12:
        msg += 'Good Morning'
    elif h<16:
        msg += 'Good Afternoon'
    elif h<21:
        msg += 'Good NIGHT'
    else:
        'good night'
    msg += '</h1><hr>'
    msg += '<h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)


