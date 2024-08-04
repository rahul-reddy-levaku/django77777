from django.shortcuts import render
import datetime

# Create your views here.
def info_view(request):
    time = datetime.datetime.now()
    name = 'Django'
    prerequisite='python'
    my_dict={'NAME':name,'time':time,'prerequisite':prerequisite}
    return render(request,'testapp/results.html',my_dict)