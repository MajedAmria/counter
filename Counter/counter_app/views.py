from http.client import HTTPResponse
from django.shortcuts import render

def display():

    return HTTPResponse("hello")

def show(request):
    request.se