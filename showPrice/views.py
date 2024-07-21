from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from . import models
import jdatetime
# Create your views here.
def index(request):
    today=jdatetime.date.today()
    allcategory = models.category.objects.all()
    allCurrency = models.Currency.objects.filter(category=allcategory[0]).filter(pubDate=today).all()

    return render(request=request,template_name='index.html',context={'currencies':allCurrency,'categories':allcategory,'today':today})
def requestCurrency(request):
    if request.method == 'POST':
        clock=request.POST['clock']
        category=request.POST['category']
        if clock !='':
            Currency = models.Currency.objects.filertDat(pubDate=clock).all()
            category1 = models.category.objects.filter(category=category).all()
            return JsonResponse({'data':Currency,'category':category1})
        else:
            return JsonResponse({'data':False})
    else:
        return JsonResponse({'data':False})