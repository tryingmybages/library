from django.db import models

# Create your models here.

class Categrymodel(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name
    




class Book(models.Model):
    x=[
        ('availble','availble'),
        ('retaled','retaled'),
        ('seald','seald')
    ]
    title = models.CharField(max_length=220)
    outher = models.CharField(max_length=50,null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retalprice = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retalperiod = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    outherimage = models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices= x ,null=True,blank=True)
    Categry =models.ForeignKey(Categrymodel, on_delete= models.PROTECT,null=True,blank=True)
    def __str__(self) :
        return self.title
    
