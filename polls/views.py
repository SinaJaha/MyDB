#from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    text = """<h1>welcome to my app !</h1>\n
    <h2>hello world !</h2>\n
    <p> This is the polls index page.</p>"""
    return HttpResponse(text)


def myapp(request):
    text = """<h1>welcome to my app !</h1>\n
    <p>This is the site for my app.</p>"""
    return HttpResponse(text)