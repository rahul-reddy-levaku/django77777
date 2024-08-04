from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q,Avg,Max,Min,Sum,Count
from django.db.models.functions import Lower
def retrieve_view(request):
    #emp_list = Employee.objects.all()
    #emp_list= Employee.objects.filter(esal__gt=15000)
    #emp_list= Employee.objects.filter(esal__gte=15000)
    #emp = Employee.objects.get(id__exact=52)
    #emp_list = Employee.objects.filter(ename__contains='john')
    #emp_list = Employee.objects.filter(id__in=[1,51,52])
    #emp_list = Employee.objects.filter(ename__startswith='s')
    #emp_list = Employee.objects.filter(ename__endswith='S')
    #emp_list = Employee.objects.filter(esal__range=[12000,15000])
    #emp_list = Employee.objects.filter(ename__startswith='a')
    #emp_list = Employee.objects.filter(esal__lte=15000)
    #emp_list = Employee.objects.filter(ename__startswith='A')  |  Employee.objects.filter(esal__lte=11000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D')|Q(esal__lte=12000))
    #emp_list = Employee.objects.filter(ename__startswith='S')&Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='a')&Q(esal__lt=18000))
    #emp_list = Employee.objects.filter(ename__startswith='s',esal__lt=18000)
    #emp_list = Employee.objects.exclude(ename__startswith='s')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='d'))
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #emp_list = Employee.objects.all().values('ename','esal')
    #emp_list = Employee.objects.create(eno=2345,ename='kareena',esal=123.0,eaddr='chennai')
    #emp_list = Employee.objects.all().only('ename','esal')
    #emp_list = Employee.objects.all().order_by(Lower('ename'))
    s1 = Employee.objects.filter(esal__lte=12000)
    s2 = Employee.objects.filter(ename__startswith='S')
    s3 = s1.union(s2)
    emp_list = s3
    return render(request,'testapp/specificcolumns.html',{'emp_list':emp_list})
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)