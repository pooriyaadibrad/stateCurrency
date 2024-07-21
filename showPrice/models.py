from django.db import models
from django_jalali.db import models as jalali_models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=50)
    sell=models.DecimalField(max_digits=10,decimal_places=1)
    buy=models.DecimalField(max_digits=10,decimal_places=1)
    pubDate=jalali_models.jDateField(auto_now_add=True)
    category=models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
class category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
