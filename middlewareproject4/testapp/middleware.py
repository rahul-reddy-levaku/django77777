from django.http import HttpResponse
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line before preprocessing')
        response = self.get_response(request)
        print('After preprocessing')
        return response
class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line by middleware2')
        response = self.get_response(request)
        print("this after")
        return response