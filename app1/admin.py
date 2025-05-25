from django.contrib import admin
from .models import Department,Role,Employee

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = [i.name for i in Department._meta.fields]

class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = [i.name for i in Role._meta.fields]

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = [i.name for i in Employee._meta.fields]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)