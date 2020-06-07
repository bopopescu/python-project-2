from .models import Users,EmployeeDetails
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class EmmployeeDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDetails
        fields = '__all__'