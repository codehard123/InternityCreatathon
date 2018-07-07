from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name=models.CharField(max_length=100,blank=False)
    location_address=models.CharField(max_length=20,blank=True)
    number_of_dustbin=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Vote(models.Model):
    location= models.ForeignKey(Location,on_delete=models.CASCADE, related_name="Vote_location")        
    date= models.DateField()
    votes= models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.location.name
    
class VoteLog(models.Model):
    location=models.ForeignKey(Location,on_delete=models.CASCADE, related_name="Vote_log")
    voted= models.BooleanField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location.name
    
    #coded by RAJAT JAIN