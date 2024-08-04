from django.shortcuts import render

# Create your views here.
def result_view(request):
    subjects = {'s1':'python','s2':'Django','s3':'Restapi','s4':'Mongodb'}
    return render(request,'testapp/results.html',subjects)