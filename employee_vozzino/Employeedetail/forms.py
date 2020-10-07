from django.forms import ModelForm
from Employeedetail.models import *
from django  import forms

class Employeecreateform(ModelForm):
    Confirmpassword = forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model = Employee
        fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password", "Confirmpassword"]
        # fields = ["Name", "Telephone","Age","Profile_pic", "Email", "Username", "Password","Confirmpassword"]
    def clean(self):
        cleaned_data=super().clean() #mandatory
        Name=cleaned_data.get("Name")
        Telephone=cleaned_data.get("Telephone")
        Age = cleaned_data.get("Age")
        Email=cleaned_data.get("Email")
        # Profile_pic=cleaned_data.get("Profile_pic")
        Username=cleaned_data.get("Username")
        Password=cleaned_data.get("Password")
        Confirmpassword=cleaned_data.get("Confirmpassword")

        if Password!=Confirmpassword:
            msg="Pls enter a valid password"
            self.add_error("Password",msg)

class Employeelogin(forms.Form):
    Username=forms.CharField(max_length=200,)
    Password=forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model=Employee
        fields=['Username','Password',]

    def clean(self):
        cleaned_data=super().clean() #mandatory
        Username = cleaned_data.get("Username")
        # print(Username)
        # qs=Users.objects.get(Username==Username)
        # print("sss",qs.Username)
        # Password = cleaned_data.get("Password")
        # if(Users.objects.get(Username==Username)):
        #     print(Username)
        #     pass
        # else:
        #     msg="No user exist in this name"
        #     self.add_error('Username',msg)