from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>This is my first project in specific urls in app1</h1>')
