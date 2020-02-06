from django.utils.timezone import get_current_timezone
from django.http import HttpResponse
import datetime

def default_view(request) :
    date = datetime.datetime.now()
    origin_date = date.strftime("%B, %a %d %Y")

    html = f"<h3>[ Work Perfectly ]</h3><span>Date : {origin_date}</span>"
    return HttpResponse(html)