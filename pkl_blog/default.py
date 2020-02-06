from django.shortcuts import render
import datetime, sys
sys.path.append('../dist/template/')

def default_view(request) :
    return render(request, 'index.html')