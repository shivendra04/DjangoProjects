from django.db import models
'''
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')
    def get_emp_sal_range(self,esal1,esal2):
        return super().get_queryset().filter(esal__range=(esal1,esal2)).order_by('esal')
    def get_employee_sorted_by(self,param):
        return super().get_queryset().order_by(param)
'''
class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-esal')

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')


# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=356)
    objects=CustomManager1()

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
