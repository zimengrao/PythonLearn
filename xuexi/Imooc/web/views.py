from django.shortcuts import render
from django.http.response import HttpResponse
import json

# Create your views here.
def login(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        data = request.GET.get('data')
        result['user'] = username
        result['mobileNum'] = mobile
        result['data'] = data
        result = json.dumps(result)
        return HttpResponse(request,content_type='application/json;charset=utf-8')
