from django.contrib import admin
from testApp.models import Company

# Register your models here.
class companyAdmin(admin.ModelAdmin):
    list_display=['name','location','Ceo']

admin.site.register(Company,companyAdmin)
