
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from Employeedetail.models import *
from Employeedetail.forms import *

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FileUploadParser
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from Employeedetail.models import Employee
from Employeedetail.serializers import EmployeeSerializer


class createEmployee(TemplateView):
    form_class=Employeecreateform
    model_name=Employee
    template_name = "Employeedetail/Employeecreate.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Telephone = form.cleaned_data["Telephone"]
            Age = form.cleaned_data["Age"]
            # if 'Profile_pic' in request.FILES:
            #     Profile_pic = request.FILES['Profile_pic']
            # Profile_pic = form.cleaned_data["Profile_pic"]
            Email = form.cleaned_data["Email"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            # isActive=True
            qs = Employee.objects.create(Name=Name, Telephone=Telephone,Age=Age,\
                    Email=Email,Username=Username,Password=Password,isActive=True)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            return render(request, self.template_name,{"form":form})

class loginEmployee(TemplateView):
    form_class=Employeelogin
    model_name=Employee
    template_name = "Employeedetail/Employeelogin.html"
    template_name1 = "Employeedetail/home.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("Hi0000")
        if form.is_valid():
            print("Hi1111")
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            qs=Employee.objects.get(Username=Username)
            print("Hi")
            print("Active:",qs.isActive)
            if((qs.Username==Username)&(qs.Password==Password)):
                request.session['Username']=Username
                context = {}
                context["qs"] = qs
                # context["user"] = user
                print("hiiiiiiiiiiiiii")
                return render(request, self.template_name1, context)
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                print("Hi2222")
                return redirect("User_login")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            print("Hi33333")
            return render(request, self.template_name,{"form":form})

class viewEmployee(TemplateView):
    model_name=Employee
    template_name = "Employeedetail/Employeeview.html"
    # Username = request.session["Username"]
    # def get_queryset(self):
    #
    #     return self.model_name.objects.filter(Username=request.session["Username"])
    def get(self, request, *args, **kwargs):
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        qs=Employee.objects.all()
        print("ddddd")
        context={}
        context["viewemployee"]=qs
        return render(request,self.template_name,context)

def logoutEmployee(request):
        del request.session['Username']
        return redirect("Employee_login")
class updateEmployee(UpdateView):
    model=Employee
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password"]
    success_url = '/Employeeview'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'Employeedetail/Employee_update.html'
class deleteEmployee(DeleteView):
    model = Employee
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password"]
    # template_name_suffix = "_del"
    success_url = '/Employeeview'
class EmployeeList(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self,request):
        serializer = EmployeeSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.data, status=400)

class EmployeeListCreateAPIView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    serializer_class =  EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        documents = Employee.objects.all()
        serializer = EmployeeSerializer(documents,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)