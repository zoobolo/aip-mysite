from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Airport(models.Model):
    # username = models.ManyToManyField(User)
    airport_name = models.CharField("Airport Name",max_length=50)
    airport_locid = models.CharField("LOCID",max_length=3)  
    list_display = ('airport_name', 'airport_locid')
    ado_pm = models.CharField("Ado Program Manager",max_length=20)
    # airport_engineer = models.ForeignKey(User)
    # airport_planner = models.ForeignKey(User)
    # airport_environmental = models.ForeignKey(User)
    
    
    def __str__(self):
        # return (self.airport_name)
        return '%s %s'  % (self.airport_name, self.airport_locid)
        
class Grant(models.Model):
    airport = models.ForeignKey(Airport,on_delete=models.CASCADE,default=None) 
    grant_number = models.CharField("Grant Number",max_length=200)
    grant_amount = models.DecimalField("Grant Amount",max_digits=10, decimal_places=2)
#    grant_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.grant_number
        
class Project(models.Model):
    airport = models.ForeignKey(Airport,on_delete=models.CASCADE)
    grant = models.ForeignKey(Grant,on_delete=models.CASCADE)
    project_description = models.CharField("Project Description",max_length=200)
    
    def __str__(self):
        # return self.project_description
       return '%s %s'  % (self.grant, self.project_description) 
       
class Sponsor(models.Model):
    airport = models.ManyToManyField(Airport) 
    username = models.ManyToManyField(User)
    sponsor_name = models.CharField("Sponsor Name",default=None,blank=True,max_length=200)
    sponsor_type = models.CharField("Sponsor Type",default=None,blank=True,max_length=200)
    sponsor_addr1 = models.CharField("Sponsor Address 1",default=None,blank=True,max_length=200)
    sponsor_addr2 = models.CharField("Sponsor Address 2",default=None,blank=True,max_length=200)
    sponsor_addr3 = models.CharField("Sponsor Address 3",default=None,blank=True,max_length=200)
    sponsor_city = models.CharField("Sponsor City",default=None,blank=True,max_length=200)
    sponsor_state = models.CharField("Sponsor State",default=None,blank=True,max_length=200)
    sponsor_zip = models.CharField("Sponsor Zip",default=None,blank=True,max_length=200)
    sponsor_county = models.CharField("Sponsor County",default=None,blank=True,max_length=200)
    sponsor_DUN = models.IntegerField("DUN Number",blank=True,null=True)
    sponsor_ADO = models.CharField("ADO",default=None,blank=True,max_length=200)

    def __str__(self):
       return '%s %s'  % (self.sponsor_name, self.sponsor_addr1) 
        # return self.sponsor_name
    
class Report (models.Model):
    grant = models.ForeignKey(Grant,on_delete=models.CASCADE)
    report_type = models.CharField("Report Type",max_length=200) 
    report_doc = models.FileField(upload_to='uploads/',default=None)   
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)