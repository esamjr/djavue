from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import get_current_timezone
import sys, datetime

def default_view(request) :
    date = datetime.datetime.now()
    origin_date = date.strftime("%B, %a %d %Y")
    html = f"<h3>[ Work Perfectly ]</h3><span>Date : {origin_date}</span>"
 
    return HttpResponse(html)
