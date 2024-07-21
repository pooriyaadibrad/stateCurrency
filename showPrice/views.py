from django.shortcuts import render
import pandas as pd
from . import models
import jdatetime
# Create your views here.
def index(request):
    today=jdatetime.date.today()
    time=jdatetime.datetime.now().hour,jdatetime.datetime.now().minute,jdatetime.datetime.now().second
    time=f'{time[0]}:{time[1]}:{time[2]}'
    allCurrency = models.Currency.objects.filter(pubDate=today).all()
    allcategory=models.category.objects.all()
    return render(request=request,template_name='index.html',context={'currencies':allCurrency,'categories':allcategory,'today':today,'time':time})