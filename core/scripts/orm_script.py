from core.models import Restaurent,Rating
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection
def run():
  # Restaurent.objects.create(
  #   name="Pizza Shop",
  #   date_opened=timezone.now(),
  #   longitude=54,
  #   latitude=60,
  #   restaurent_type=Restaurent.RestaurentType.MEXICAN
    
  # )
  
  # restaurent=Restaurent.objects.all()
  # print(restaurent)
  
  # print(Restaurent.objects.count())
  # print(Restaurent.objects.last())
  
  # restaurent=Restaurent.objects.first()
  # user=User.objects.first()
  # Rating.objects.create(user=user,restaurent=restaurent,rating=4)
  # print(Rating.objects.filter(rating=4))
  # print(Rating.objects.filter(rating=3))
  print(Rating.objects.exclude(rating=3))
  print(connection.queries)

