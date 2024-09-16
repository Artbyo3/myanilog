from django.shortcuts import render
from django.http import HttpResponse


def home(reques):
    return HttpResponse('<h1>home are you there???</h1>')
