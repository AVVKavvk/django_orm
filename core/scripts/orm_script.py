import asyncio
from django.db import connection
from django.db.models import Min, Max, Avg, Sum,Value,CharField,Count,F,Q
from django.db.models.functions import  Length , Concat ,Coalesce
from core.models import Restaurent,Rating,Sale
from core.models import Sale
from pprint import pprint
from django.utils import timezone
import random

def run():
  # Restaurent.objects.update(capacity=None)
  # print(Restaurent.objects.aggregate(sum=Coalesce(Sum('capacity'),0)))
  # print(Restaurent.objects.aggregate(sum=Sum('capacity',default=0)))
  # restaurants=Restaurent.objects.filter(capacity__isnull=False).order_by('capacity').values('capacity')
  # restaurants=Restaurent.objects.order_by(F('capacity').asc(nulls_last=True)).values('capacity')
  # print(restaurants)
  # restaurant=Restaurent.objects.first()
  # restaurant2=Restaurent.objects.last()
  # restaurant.capacity=20
  # restaurant2.capacity=30
  # restaurant.save()
  # restaurant2.save()
  # restaurants=Restaurent.objects.filter(capacity__isnull=True)
  # for r in restaurants:
  #   print(r.name)
  # is_profited=Q(income__gt=F('expenditure'))
  # is_name_contains_num=Q(restaurent__name__regex=r"[0-9]+")
  
  # sales=Sale.objects.select_related('restaurent').filter(is_profited & is_name_contains_num)
  # # print(sales)
  # for s in sales:
  #   print(s.restaurent.name,"  ",s.income-s.expenditure)
  
  # it_or_mex=Q(name__icontains='italian') | Q(name__icontains='mexican')
  # recently_opend=Q(date_opened__gte=timezone.now()-timezone.timedelta(days=30))
  
  # restaurant=Restaurent.objects.filter(it_or_mex | recently_opend)
  
  # for r in restaurant:
  #   print(r.name)
  # it=Restaurent.RestaurentType.ITALIAN
  # mex=Restaurent.RestaurentType.MEXICAN
  
  # restaurents=Restaurent.objects.filter(Q(restaurent_type=it)| Q(restaurent_type=mex))
  # for r in restaurents:
  #   print(r.name,"  ",r.restaurent_type)
  # sales=Sale.objects.annotate(profit=F('income')-F('expenditure')).filter(profit__gt=0).order_by("-profit")
  
  # for s in sales:
  #   print(s.profit)
  
  # sales=Sale.objects.all()
  
  # for s in sales:
  #   s.expenditure=random.uniform(5,100)
    
  # Sale.objects.bulk_update(sales,['expenditure'])  
  pprint(connection.queries)
  
  
  
  
  
  
  
  
  
  
  # restaurent=Restaurent.objects.annotate(total_sale=Sum('sales__income')).order_by('-total_sale')
  # # restaurent=Restaurent.objects.annotate(total_sale=Sum('sales__income')).order_by('total_sale')
  
  # for r in restaurent:
  #   print(r.name,r.total_sale)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  # restaurent=Restaurent.objects.annotate(num=Count('ratings'),avg=Avg('ratings__rating'))
  # for r in restaurent:
  #   print(r.name, "  ",r.num,"  ",r.avg)
  
  # restaurent=Restaurent.objects.values('restaurent_type').annotate(
  #   num=Count('ratings'),
  # )
  # print(restaurent)









  # filter=Concat('name',Value('[ Ratings :'),Avg('ratings__rating'),Value(' ]'),output_field=CharField())
  # restaurent=Restaurent.objects.annotate(message=filter)
  
  # for r in restaurent:
  #   print(r.message)
















# async def custom():
  
  
  # restaurent=Restaurent.objects.annotate(len_name=Length('name')).first()
  # # print(restaurent.values('name','len_name'))
  # print(restaurent.len_name,restaurent.name)
    # Await the asynchronous aggregate function
    # result = await Sale.objects.aaggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income')
    # )
    # one_month_ago=timezone.now()-timezone.timedelta(30)
    # sale=Sale.objects.filter(datetime__gte=one_month_ago)
    # result = await sale.aaggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income')
    # )
    # print(result)
    # Note: connection.queries will not capture queries in an async context
    # Instead, use logging or debugging tools if needed

# def run():
#     filter=Concat('name',Value('[ Ratings :'),Avg('ratings__rating'),Value(' ]'),output_field=CharField)
#     restaurents=Restaurent.objects.annotate(message=filter)
  
#     for r in restaurents:
#         print(r.message)
    
    # Run the async function within an event loop
    # asyncio.run(custom())
    # restaurent=Restaurent.objects.annotate(len_name=Length('name')).first()
    # # print(restaurent.values('name','len_name'))
    # print(restaurent.len_name,restaurent.name)
  
# if __name__ == "__main__":
#     run()



































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
  # print(Rating.objects.exclude(rating=3))
  
  # restaurent=Restaurent.objects.first()
  # print(restaurent.name)
  # restaurent.name="Name Changed"
  # restaurent.save()
  
  # restaurent=Restaurent.objects.first()
  # print(restaurent.ratings.all())
  # pprint(connection.queries)
  
  # Sale.objects.create(
  #   restaurent=Restaurent.objects.first(),
  #   income=12.2,
  #   datetime=timezone.now()
    
  # )
  
  # Sale.objects.create(
  #   restaurent=Restaurent.objects.first(),
  #   income=16.8,
  #   datetime=timezone.now()
    
  # )
  
  # Sale.objects.create(
  #   restaurent=Restaurent.objects.first(),
  #   income=5.2,
  #   datetime=timezone.now()
    
  # )
  
  # print(Sale.objects.all())
  # restaurent=Restaurent.objects.first()
  # user=User.objects.first()
  # Rating.objects.get_or_create(
  #   restaurent=restaurent,
  #   user=user,
  #   rating=3
  # )    
  # user=User.objects.first()
  # restaurent=Restaurent.objects.first()
  # Rating.objects.create(
  #   user=user,
  #   restaurent=restaurent,
  #   rating=8 
    
  # )
  # rating=Rating()
  # rating.user=user
  # rating.restaurent=restaurent
  # rating.rating=9
  
  # rating.full_clean()
  # rating.save()
  # restaurent.name="Kumawat"
  # restaurent.latitude=70
  # restaurent.longitude=-150
  # restaurent.type=Restaurent.RestaurentType.INDIAN
  # restaurent.website="https://vipinnotes.onrender.com"
  # restaurent.full_clean()
  # restaurent.save()
  # restaurent=Restaurent.objects.filter(name__startswith="M")
  # print(restaurent)
  
  # restaurent.update(
  #   website="https://demo.com"
  # )
  
  # restaurent=Restaurent.objects.first()
  # # print(restaurent.name)
  # # print(restaurent.ratings.all())
  # restaurent.delete()
  
  
  
  # Indain=Restaurent.RestaurentType.INDIAN
  # Italian=Restaurent.RestaurentType.ITALIAN
  # Chinese=Restaurent.RestaurentType.CHINESE
  # restaurant=Restaurent.objects.filter(restaurent_type__in=[Indain,Italian,Chinese])
  # print(restaurant)
  # print(restaurant.count())
  
  # sales=Sale.objects.filter(income__range=(50,60))
  # print(sales)
  # print(sales.count())
  # restaurants=Restaurent.objects.values('name').first()
  # print(restaurants)
  # print(type(restaurants))
  

