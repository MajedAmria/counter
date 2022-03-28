from http.client import HTTPResponse
from django.shortcuts import render


def show(request):
    if request.session:
        request.session['time'] +=1
    else:
        request.session['time'] = 1
    
    return render(request, 'index.html')