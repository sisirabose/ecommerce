from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import customer_table,prodtable,Category,Subcategory
from .serializers import sign_serializer,prod_serializer
from rest_framework.views import APIView
from  datetime import datetime,date
from django.db.models.fields import DateField
from rest_framework.response import Response

@api_view(['POST'])
def insert(request): 
  if request.method =='POST':
       na=request.data.get('cusname')
       em=request.data.get('email')
       pa=request.data.get('password')
       im=request.data.get('image')
       k=customer_table(cusname=na,email=em,password=pa,image=im)
       k.save() 
       ob=customer_table.objects.all()
       d=sign_serializer(ob,many=True)
       return Response(d.data) 
  return Response("Enter Full Details") 


@api_view(['POST'])
def delete_user(request,pid):
     k=customer_table.objects.get(id=pid)
     k.delete()
     return Response("user"+k.name+"deleted")  


@api_view(['POST'])
def update_user(request,userid):
 k=customer_table.objects.filter(id=userid).values()
 if request.method=='POST':
       na=request.data.get('cusname')
       em=request.data.get('email')
       pa=request.data.get('password')
       im=request.data.get('image')
       k.update(cusname=na,email=em,password=pa,image=im) 
       ob=customer_table.objects.all()
       d=sign_serializer(ob,many=True)
       return Response(d.data)
 return Response("edited")


@api_view()  
def first(request):
    ob=customer_table.objects.all()
    d=sign_serializer(ob,many=True)
    return Response(d.data)


@api_view(['POST'])
def addproduct(request):

      if request.method =='POST':
       na=request.data.get('Name')
       cat=request.data.get('Category')
       scat=request.data.get('Subcategory')
       ca=Category.objects.get(cname=cat)
       sa=Subcategory.objects.get(sname=scat)
       brand=request.data.get('Brand')
       pr=request.data.get('Price')
       qu=request.data.get('Quantity')
       cna=request.data.get("cusname")
       cust=customer_table.objects.get(id=cna)
       date1=date.today()
       im=request.data.get('Image')
       prodtable.objects.create(Name=na,Category=ca,Subcategory=sa,Quantity=qu,Price=pr,Image=im,Brand=brand,edate=date1,cusname=cust) 
       k=prodtable.objects.all()
       res=prod_serializer(k,many=True)
       return Response(res.data)
      return Response("Please fill form correctly")



@api_view() 
def prodview(request):
    ob=prodtable.objects.all()
    d=prod_serializer(ob,many=True)
    return Response(d.data)

@api_view(['GET','PUT'])
def update_product(request,proid):
    k=prodtable.objects.filter(id=proid)
    if request.method=='PUT':  
       na=request.data.get('Name')
       cat=request.data.get('Category')
       scat=request.data.get('Subcategory')
       ca=Category.objects.get(cname=cat)
       sa=Subcategory.objects.get(sname=scat)
       brand=request.data.get('Brand')
       pr=request.data.get('Price')
       qu=request.data.get('Quantity')
       cna=request.data.get("customer_name")
       cust=customer_table.objects.get(name=cna)
       date1=date.today()
       im=request.data.get('Image')
       k.update(Name=na,Category=ca,Subcategory=sa,Quantity=qu,Price=pr,Image=im,Brand=brand,edate=date1,customer_name=cust) 
       res=prod_serializer(k,many=True)
       return Response(res.data)
    return Response("Please fill form correctly")



@api_view(['GET','POST'])
def delete_product(request,proid):
    prod=prodtable.objects.get(id=proid)
    Name=prod.Name
    prod.delete()
    return Response("product:"+Name+" is deleted")

@api_view(['GET','POST'])
def actvestatus(request):
    if request.method=="POST":
        pid=request.data.get("id")
        p=prodtable.objects.get(id=pid)
        da1=p.entered_date
        
        print("date#################",da1)
       
        a = datetime.datetime.today()
        print("+++++++++++++++++++++++",a)
        y=a.year
        d=a.day
        m=a.month
        ab= date(y,m,d)
        print("%%%%%%%%%%%%%",ab)
        
        da2=da1.year
        da3=da1.month
        da4=da1.day
        ba = date(da2,da3,da4)
        print("%%%%%%%%%%%%%%%%",ba)
        diff=ab-ba
        
  
        print('Difference$$$$$$$$$$$$$$$$$$$$: ', diff.days)
        diff=int(diff.days)
        if int(diff)>60:
            p.status=0
            p.save()
            return Response("product disabled!!")
        else:
            p.status=1
            p.save()
            return Response("Product active")
    return Response("fill form!")      