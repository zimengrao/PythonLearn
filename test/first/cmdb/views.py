from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

# def hello(request):
#     return HttpResponse("Hello world!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    return HttpResponse(str(c))
