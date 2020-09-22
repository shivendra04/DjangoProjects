from django.contrib import admin
from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','eaddr','esal']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
