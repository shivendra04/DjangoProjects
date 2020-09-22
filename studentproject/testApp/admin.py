from django.contrib import admin
from testApp.models import student
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
# Register your models here.
admin.site.register(student,StudentAdmin)
