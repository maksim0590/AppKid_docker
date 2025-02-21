from . import views
from django.http import HttpResponse

class  TaskMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        a = 5

        response = self.get_response(request)
        
        return response