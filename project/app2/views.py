
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Welcome to Home3 app index Page")

