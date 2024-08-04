from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request, 'testapp/index.html')


def movies_view(request):
    head_msg = 'Movies informatio'
    sub_msg1 = 'og'
    sub_msg2 = 'de'
    sub_msg3 = 'pl'
    type='movies'
    my_dict = {'head_msg':head_msg,'sub1':sub_msg1,'sub2':sub_msg2,'sub3':sub_msg3,'type':type}
    return render(request, 'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'Sports information'
    sub_msg1 = 'yesterdsy'
    sub_msg2 = 'today match'
    sub_msg3 = 'who will win '
    type='sports'
    my_dict = {'head_msg':head_msg,'sub1':sub_msg1,'sub2':sub_msg2,'sub3':sub_msg3,'type':type}
    return render(request, 'testapp/news.html',my_dict)

def politics_view(request):
    head_msg = 'politics information'
    sub_msg1 = 'yest'
    sub_msg2 = 'today match'
    sub_msg3 = 'who will win '
    type='politics'
    my_dict = {'head_msg':head_msg,'sub1':sub_msg1,'sub2':sub_msg2,'sub3':sub_msg3,'type':type}
    return render(request, 'testapp/news.html',my_dict)