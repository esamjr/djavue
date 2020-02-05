from django.shortcuts import render
from django.http import HttpResponse
import sys, datetime

def default_view(request) :
    date = datetime.datetime.now()
    html = "<h3>[ Work Perfectly ]</h3><span>Date : %s</span>" % date
    return HttpResponse(html)
