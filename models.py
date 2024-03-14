from django.db import models
from django import forms




class home(models.Model):
    #  Id = models.IntegerField()
    Firstname = models.CharField(max_length=150)
    Middlename = models.CharField(max_length=500)
    Lastname = models.CharField(max_length=15)

    Phone = models.IntegerField(max_length=50, default='')
    Email = models.CharField(max_length=50, default='')
    userid = models.CharField(max_length=50, default='')
    Password= models.CharField(max_length=50, default='')

    #  companylogo =models.FileField()

    def __str__(self):
        return self.companyName

    ddlcompanyobjects = models.Manager()




