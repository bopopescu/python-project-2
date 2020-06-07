from django.db import connections
from django.db import models
from phone_field import PhoneField
from enum import Enum
from phone_field import phone_number
class UserType(Enum):
    AD="Admin"
    HR="Hr"
    EMPLOYEE="Employee"

class Sex(Enum):
    MALE="Male"
    FEMALE="Female"

class MarriedStatus(Enum):
    NO="No"
    YES="Yes"

# Create your models here.

class Users(models.Model):
    #id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    userType = models.CharField(max_length=10, null=True, choices=[(tag, tag.value) for tag in UserType])

    class Meta:
        db_table = "users"

class EmployeeDetails(models.Model):

    name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    Address = models.CharField(max_length=100)
    Sex = models.CharField(max_length=10, null=True, choices=[(tag, tag.value) for tag in Sex])
    email = models.EmailField(primary_key=True,max_length=50, null=False)
    married = models.CharField(max_length=10, null=True, choices=[(tag, tag.value) for tag in MarriedStatus])
    user = models.OneToOneField(Users, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "EmployeeDetails"








