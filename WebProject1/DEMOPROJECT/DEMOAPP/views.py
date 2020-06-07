from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Users, EmployeeDetails
import sys


def login(request):
    context = {}
    loginuser = None
    if request.method == 'POST':
        try:
            user = Users.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
            if user != None:
                usertype = user.userType
                # Need to investigate
                #request.session['loggeduser'] = user.id
                if usertype != None and usertype == "Admin":
                    return render(request, 'DEMOAPP/admin.html', {'loggeduser': user})
                # return render(request, 'DEMOAPP/admin.html')
                elif usertype != None and usertype == "Hr":
                    return render(request, 'DEMOAPP/hr.html', {'loggeduser': user})
                else:
                    context['errorstr'] = "Invalid User Type"
                    return render(request, 'DEMOAPP/login.html', context)
        except:
            context['errorstr'] = "Password don't match"
            print("Error", sys.exc_info()[0])
            return render(request, 'DEMOAPP/login.html', context)
    else:
        return render(request, 'DEMOAPP/login.html', context)


def register(request):
    context = {}
    if request.method == 'POST':
        try:
            user = Users()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.userType = request.POST.get('usertype')
            user.save()
            employee = EmployeeDetails()
            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')
            employee.Address = request.POST.get('address')
            employee.sex = request.POST.get('sex')
            employee.email = request.POST.get('email')
            employee.married = request.POST.get('married')
            employee.user_id = user.id
            employee.save()

            context['errorstr'] = "User created."
            return render(request, 'DEMOAPP/admin.html', context)
        except:
            print("Error", sys.exc_info()[0])
            context['errorstr'] = "Unable to Create User. Try Again!"

    return render(request, 'DEMOAPP/register.html', context)

def viewemployees(request):
    users = Users.objects.all()
    print(users[2].employeedetails)
    return render(request,'DEMOAPP/view-employees.html', {'userlist': users})