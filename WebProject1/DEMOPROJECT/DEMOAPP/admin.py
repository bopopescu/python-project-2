from django.contrib import admin

from .models import Users,EmployeeDetails

# Register your models here.
admin.site.register(Users)
admin.site.register(EmployeeDetails)
