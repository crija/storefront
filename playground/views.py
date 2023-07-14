from django.shortcuts import render
from django.http import HttpResponse

def calculete():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculete()
    return render(request, 'hello.html', {'name':'Mosh'})