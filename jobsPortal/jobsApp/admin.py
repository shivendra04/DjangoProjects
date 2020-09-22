from django.contrib import admin
from jobsApp.models import hydjobs,chennaijobs,banglorejobs,punejobs

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']



# Register your models here.
admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(banglorejobs,banglorejobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
