from rest_framework.serializers import ModelSerializer
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from Employeedetail.models import Employee




class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'