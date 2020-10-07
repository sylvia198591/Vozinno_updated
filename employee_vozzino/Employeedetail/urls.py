"""Employee URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Employeedetail import views
from Employeedetail.views import *
urlpatterns = [
    path('Registration',views.createEmployee.as_view(),name="Employee_create"),
    # path('Registration', lambda request:(views.createEmployee.as_view())\
    #         if ('Username' not in request.session) else \
    #             redirect('Employee_home'),name="Employee_create"),
    path('Login', views.loginEmployee.as_view(), name="Employee_login"),
    path('Logout', lambda request:redirect('Employee_home') \
        if ('Username' not in request.session) else \
            (logoutEmployee(request)), name="Employee_logout"),
    # path('Home', index.html, name="Home"),
    path("Loggedin",lambda request:render(request,"index.html"),name="Employee_home_loggedin"),
    # path("Employeeview",lambda request:render(request,"index.html"),name="Employee_home_loggedin"),
    path('Employeeview',lambda request:redirect('Employee_login') \
        if ('Username' not in request.session) else \
            (views.viewEmployee.as_view()(request)), name="Employee_view"),
    path('Editemployee/<int:pk>', views.updateEmployee.as_view(), name="Employee_edit"),
    path('Deleteemployee/<int:pk>', views.deleteEmployee.as_view(), name="Employee_delete"),
    path("", lambda request: redirect('Employee_login') \
        if ('Username' not in request.session) else \
        redirect('Employee_home_loggedin')
         , name="Employee_home"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)