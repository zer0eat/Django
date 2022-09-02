from multiprocessing import context
from unittest.loader import VALID_MODULE_NAME
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # 1번
    # name = 'young'
    # context = {
    #     'name' : name
    # }
    # 2번
    context = {
        'name' : 'YOUNG',
        'age' : [0, 1],
        'foods' : ['apple', 'banana', 'pizza'],
    
    }
    return render(request, 'dtl.html', context)

def greeting(request):
    # 1번
    # name = 'young'
    # context = {
    #     'name' : name
    # }
    # 2번
    context = {
        'name' : 'YOUNG',
        'age' : [0, 1],
        'foods' : ['apple', 'banana', 'pizza'],
    
    }
    return render(request, 'greeting.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    value = request.GET.get('search')
    name = 'young'
    context = {
        'value' : value,
        'name' : name,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'catch.html', context)