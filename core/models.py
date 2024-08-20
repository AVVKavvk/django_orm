from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Restaurent
# User
#

class Restaurent(models.Model):
  class RestaurentType(models.TextChoices):
    INDIAN="IN","Indian",
    CHINESE="CH","Chinese",
    ITALIAN="IT","Italian",
    MEXICAN="MX","Mexican",
    GREEK="GR" ,"Greek"
    AMERICAN="AM","American",
    OTHERS="OT","Others"
    
  name=models.CharField(max_length=100)
  website=models.URLField(default='')
  date_opened=models.DateTimeField()
  longitude=models.FloatField()
  latitude=models.FloatField()
  restaurent_type=models.CharField(max_length=2,choices=RestaurentType.choices)
  
  def _str__(self):
      return self.name
  
class Rating(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
  rating=models.PositiveSmallIntegerField()
  def __str__(self):
      return f"Rating OF :{self.rating}"
  
class Sale(models.Model):
  restaurent=models.ForeignKey(Restaurent,on_delete=models.SET_NULL , null=True)
  income=models.DecimalField(max_digits=8,decimal_places=2)
  datetime=models.DateTimeField()