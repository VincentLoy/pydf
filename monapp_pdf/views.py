from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text = "<h1>COUCOU LES ZAMIS</h1>"

    return HttpResponse(text)
