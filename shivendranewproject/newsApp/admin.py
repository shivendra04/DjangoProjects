from django.contrib import admin
from newsApp.models import student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(student)
