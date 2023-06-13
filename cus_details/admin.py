from django.contrib import admin
from cus_details.models import customer
class customerdetails(admin.ModelAdmin):
    list_display=('tableno','name','phone','gmail')
admin.site.register(customer,customerdetails)