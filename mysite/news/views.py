from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print((request))
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('<h1>Test string</h1>')

def pohuy(request):
    return HttpResponse('<h3>А мне POHUY</h3>')
