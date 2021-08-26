
from django.contrib import admin
from django.urls import path
from Ecommerce_App import views,APiView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="first"),
    path('signup',views.sign,name="signup"),
    path('login',views.login,name="login"),
    path('add',views.addcat,name="addcat"),
    path('addcat',views.addprod,name="addprod"),
    path('addsubcat',views.addsubcat,name="addsubcat"),
    path('plist',views.prolist,name="plist"),
    path('ulist',views.userlist,name="userlist"),
    path('log',views.logedout,name="logedout"),




    path('first',APiView.first,name="first"),
    path('ins',APiView.insert,name="ins"),
    path('addproducts',APiView.addproduct,name="addproducts"),
    path('dele/<int:proid>',APiView.delete_product,name="dele"),
    path('upd/<int:proid>',APiView.update_product,name="upd"),
]
