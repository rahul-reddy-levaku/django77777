from django.shortcuts import render
from testapp.forms import FeedBackForm
def feedback_view(request):
    submitted = False
    name = ''

    form = FeedBackForm(request.POST)
    if form.is_valid():
        print('Form validation success and printing feedback information')
        print('*' * 55)

        submitted = True


    return render(request, 'testapp/feedback.html',
                  {'form': form, 'submitted': submitted, 'name': name})

