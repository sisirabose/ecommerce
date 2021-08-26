from django.db import models

class customer_table(models.Model):
    cusname=models.CharField(max_length=30,null=True) 
    email=models.CharField(max_length=30,null=True) 
    password=models.CharField(max_length=30,null=True) 
    image=models.ImageField(upload_to ='media/',null=True,blank=True)   

    def __str__(self):
     return str(self.cusname) 

class Category(models.Model):  
  cname=models.CharField(max_length=30,null=True) 


  def __str__(self):
     return self.cname
 
class Subcategory(models.Model):  
  sname=models.CharField(max_length=30,null=True) 
  Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

  def __str__(self):
     return self.sname  


class prodtable(models.Model):
    Name=models.CharField(max_length=30,null=True) 
    Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    Subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True)
    cusname=models.ForeignKey(customer_table,on_delete=models.CASCADE,null=True)
    Brand=models.CharField(max_length=30,null=True) 
    Quantity=models.IntegerField(null=True) 
    Price=models.FloatField(null=True) 
    Stock=models.IntegerField(null=True) 
    Image=models.ImageField(upload_to ='product/',null=True,blank=True)  
    edate=models.DateField(null=True)
    status=models.BooleanField(null=True) 
    def __str__(self):
     return str(self.Name)  

class usertable(models.Model):
    Fname=models.CharField(max_length=30,null=True)  
    Lname=models.CharField(max_length=30,null=True)
    Email=models.CharField(max_length=30,null=True) 
    Password=models.CharField(max_length=30,null=True) 
    Rpassword=models.CharField(max_length=30,null=True) 
    Image=models.ImageField(upload_to ='media/',null=True,blank=True)    