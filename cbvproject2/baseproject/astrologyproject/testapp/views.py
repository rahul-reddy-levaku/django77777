from django.shortcuts import render
import datetime
import random

def result_view(request):
    msg_list = [
    'The golden days ahead',
    'Better to sleep more time even in class also',
    'Tomorrow will be the best day of your life',
    'Tomorrow is the perfect day to propose your gf',
    'Very soon you will get the job'
    ]
    names_list=['sunny', 'kareena', 'samantha', 'samyuktha' , 'radhika']
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h <16:
        s = 'Good Afternoon'
    elif h <21:
        s='Good Evening'
    else:
        s='Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'NAME':name,'MSG':msg,'wish':s}
    return render(request,'testapp/astro.html',my_dict)