from django.contrib import admin

from .models import customer_table,prodtable,Category,Subcategory
admin.site.register(customer_table)
admin.site.register(prodtable)
admin.site.register(Category)
admin.site.register(Subcategory)

