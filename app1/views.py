from django.shortcuts import render,redirect
from app1.models import Role,Department,Employee
from django.contrib import messages

# Create your views here.
def index(request):
    role = Role.objects.all()
    department = Department.objects.all()
    employee = Employee.objects.all()
    context = {
        'roles':role,
        'departments':department,
        'employees':employee
    }
    return render(request,'index.html',context)

def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        role_id = request.POST['role']
        dept_id = request.POST['dept']
        mobile = request.POST['mobile']
        reporting_manager = request.POST['reporting_manager']
        date_of_joining = request.POST['date_of_joining']

        department = Department.objects.get(dept_id = dept_id)
        role = Role.objects.get(role_id = role_id)
        if reporting_manager:
            reporting_manager = Employee.objects.get(employee_id=reporting_manager)
        else:
            reporting_manager = None


        print(first_name,last_name,email,date_of_joining,reporting_manager,role_id,dept_id)

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            username=username,
            role=role,
            dept=department,
            mobile=mobile,
            reporting_manager=reporting_manager,
            date_of_joining=date_of_joining
        )

        messages.success(request, f"Employee {first_name} {last_name} added successfully.")
        return redirect('index')

    
    role = Role.objects.all()
    department = Department.objects.all()
    employee = Employee.objects.all()
    context = {
        'roles':role,
        'departments':department,
        'employees':employee
    }
    return render(request,'add_employee.html',context)


def update_employee(request,id):
    role = Role.objects.all()
    employee = Employee.objects.get(employee_id =id)
    department = Department.objects.all()
    employees = Employee.objects.exclude(employee_id=id)


    if request.method == 'POST':
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.username = request.POST['username']
        employee.email = request.POST['email']
        employee.mobile = request.POST['mobile']
        employee.date_of_joining = request.POST['date_of_joining']

        dept_id = request.POST['dept']
        role_id = request.POST['role']
        reporting_manager_id = request.POST.get('reporting_manager')

        employee.dept = Department.objects.get(dept_id=dept_id)
        employee.role = Role.objects.get(role_id=role_id)

        if reporting_manager_id:
            employee.reporting_manager = Employee.objects.get(employee_id=reporting_manager_id)
        else:
            employee.reporting_manager = None  

        employee.save()
        messages.success(request, f"Employee {employee.first_name} updated successfully.")
        return redirect('index') 

    context = {
        'roles':role,
        'departments':department,
        'employee':employee,
        'employees':employees
    }
    return render(request,'update_employee.html',context)

def delete_employee(request, id):
    employee = Employee.objects.get(employee_id=id)
    employee.delete()
    messages.success(request, f"Employee {employee.first_name} {employee.last_name} deleted successfully.")
    return redirect('index')