from django.shortcuts import render, HttpResponse
from .models import Employee, Department  # , Role
from datetime import datetime
from django.db.models import Q


# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    # print(context)
    # all content of will show in  all_emp html page
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']

        last_name = request.POST['last_name']

        salary = int(request.POST['salary'])

        bonus = int(request.POST['bonus'])

        phone = int(request.POST['phone'])

        dept = int(request.POST['dept'])

        """role = int(request.POST['role'])"""
        role = (request.POST['role'])

        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary,
                           bonus=bonus, phone=phone, dept_id=dept, role=role, hire_date=datetime.now())

        new_emp.save()
        return HttpResponse('Employee added Sucessfull...')
    elif request.method == 'GET':  # show all the entry which  is we are going to fill in form
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(
                id=emp_id)  # get employee from database
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed successfully!.....")
        except:
            return HttpResponse("Please Enter Valid Employee Id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__icontains=role)
            """emps = emps.filter(role__name__icontains=role)"""
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Error occurred ")
