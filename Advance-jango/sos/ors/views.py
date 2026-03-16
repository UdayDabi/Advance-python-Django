from django.http import HttpResponse
from django.shortcuts import render



def test_ors(request):
    return HttpResponse('<h1>Hello ORS</h1>')
