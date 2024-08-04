from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    name = 'sunny'
    rollno = 101
    marks = 98
    my_dict ={"insert_date":date,'NAME':name,'ROLLNO':rollno,'MARKS':marks}
    return render(request,'testapp/wish.html',context=my_dict)