from django.contrib import admin
from testApp.models import contactinfo1,student1,teacher1
# Register your models here.
admin.site.register(contactinfo1)
admin.site.register(student1)
admin.site.register(teacher1)
'''
class ContactInfoAdmin(admin.ModelAdmin):
    list_display=['name','email','address']
class TeacherAdmin(admin.ModelAdmin):
    list_display=['subject','salary']
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','marks']
'''
