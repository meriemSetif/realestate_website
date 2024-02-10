from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>realtors page</h1>")


def realtor(request, id):
    return HttpResponse("<h1>realtor {{id}} page</h1>")


def search(request):
    return HttpResponse("<h1>realtors search page</h1>")
