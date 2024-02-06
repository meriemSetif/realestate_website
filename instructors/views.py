from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>instructors page</h1>")


def instructor(request, id):
    return HttpResponse("<h1>instructor {{id}} page</h1>")


def search(request):
    return HttpResponse("<h1>instructors search page</h1>")
