from django.shortcuts import render
from django.http import HttpResponse


def second(request):
    return HttpResponse('<h1> This is my first project in specific url app2</h1>')