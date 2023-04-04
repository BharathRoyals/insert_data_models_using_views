from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpages.objects.all()

    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)



