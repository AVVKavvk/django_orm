from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
# Create your models here.
# Restaurent
# User

def RestNameShouldStartWithCharV(name):
  if not name.startswith('V'):
    raise ValidationError("Name should start with V")
class Restaurent(models.Model):
  class RestaurentType(models.TextChoices):
    INDIAN="IN","Indian",
    CHINESE="CH","Chinese",
    ITALIAN="IT","Italian",
    MEXICAN="MX","Mexican",
    GREEK="GR" ,"Greek"
    AMERICAN="AM","American",
    OTHERS="OT","Others"
    
  # name=models.CharField(max_length=100,validators=[RestNameShouldStartWithCharV])
  name=models.CharField(max_length=100)
  website=models.URLField(default='')
  date_opened=models.DateTimeField()
  longitude=models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
  latitude=models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
  restaurent_type=models.CharField(max_length=2,choices=RestaurentType.choices)
  capacity=models.PositiveSmallIntegerField(null=True,blank=True)
  class Meta:
    ordering=[Lower('name')]
    
  def _str__(self):
      return f"{self.name}"
  
class Rating(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="ratings")
  restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE,related_name="ratings")
  rating=models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1),MaxValueValidator(5)]
  )
  def __str__(self):
      return f"Rating :{self.rating}"
  
class Sale(models.Model):
  restaurent=models.ForeignKey(Restaurent,on_delete=models.SET_NULL , null=True,related_name="sales")
  income=models.DecimalField(max_digits=8,decimal_places=2)
  expenditure=models.DecimalField(max_digits=8,decimal_places=2)
  datetime=models.DateTimeField()
  
class Staff(models.Model):
  name=models.CharField(max_length=100)
  restaurent=models.ManyToManyField(Restaurent)  