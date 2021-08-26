from django.shortcuts import render,redirect
from .models import customer_table,prodtable,Category,Subcategory,usertable
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.http import response
from django.contrib.auth import logout

def home(request):
   return render(request,'index1.html') 

def sign(request):
   if request.method =='POST':
    na=request.POST.get('name')
    em=request.POST.get('email')  
    passw=request.POST.get('password')
    im = request.FILES["image"]
    f1=FileSystemStorage()
    fr=f1.save(im.name,im)
    customer_table.objects.create(cusname=na,email=em,password=passw,image=fr) 
   return render(request,'register.html')   


def login(request):
  if request.method=='POST':
     email=request.POST.get('email')  
     password= request.POST.get('password')  
     if customer_table.objects.filter(email=email,password=password).exists():
      det=customer_table.objects.filter(email=email,password=password).values('cusname','image').first()
      request.session['cusname']=det['cusname']
      request.session['image']=det.get('image')
      count= prodtable.objects.all().count()
      count1= usertable.objects.all().count()
      return render(request,"index.html",{'count': count,'count1': count1})

     else:
       return HttpResponse("wrong user!!! Try again.. or signup ..")
      
  return render(request,"login.html")  

def addcat(request): 
 if request.method =='POST':
       ca=request.POST.get('pcat')
       k=Category(cname=ca)
       k.save()
 return render(request,'addcat.html')

def addsubcat(request): 
   c=Category.objects.all()
   if request.method =='POST':
       cat=request.POST.get('pcat')
       ca=Category.objects.get(cname=cat)
       ca1=request.POST.get('scat')
       k=Subcategory(sname=ca1,Category=ca)
       k.save()
   return render(request,'addsubcat.html',{'cat':c})

def addprod(request):
    c=Category.objects.all()
    s=Subcategory.objects.all()
    k=customer_table.objects.all()
    if request.method =='POST':
       na=request.POST.get('pname')
       cat=request.POST.get('pcat')
       scat=request.POST.get('scat')
       ca=Category.objects.get(cname=cat)
       sa=Subcategory.objects.get(sname=scat)
       brand=request.POST.get('brand')
       pr=request.POST.get('price')
       qu=request.POST.get('quan')
       stock=request.POST.get('stock')
       name1=request.session['cusname']
       cna=customer_table.objects.get(cusname=name1)
       print(name1)
       date1=date.today()
       im = request.FILES["image"]
       f1=FileSystemStorage()
       fr=f1.save(im.name,im)
       prodtable.objects.create(Name=na,Category=ca,Subcategory=sa,Quantity=qu,Price=pr,Stock=qu,Image=fr,Brand=brand,cusname=cna,edate=date1) 
    return render(request,'product.html',{'cat':c ,'scat': s})   


def prolist(request):
   k=prodtable.objects.all()
   return render(request,"prod_list.html",{'product':k})   


def userlist(request):
   k=customer_table.objects.all()
   return render(request,"viewuser.html",{'user':k})   

def logedout(request):
    if 'name' in request.session:
      logout(request)
      return redirect("login")
    else:
        return redirect("login")  

