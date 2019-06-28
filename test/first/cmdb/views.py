from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a) + int(b)
#
#     return HttpResponse(str(c))

def add1(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add1(request, a, b):
    return HttpResponseRedirect(
        reverse('add1', args=(a, b))
    )