from django.contrib import admin
from testApp.models import Employee

# Register your models here.
class EmployeeAdmion(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']

admin.site.register(Employee,EmployeeAdmion)
