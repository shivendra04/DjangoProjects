from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
from testApp.models import Employee
from django.db.models.functions import Lower
#from django.db.models.functions.base impor
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all()
    #employee=Employee.objects.get_emp_sal_range(12000, 20000)
    employee=Employee.objects.get_employee_sorted_by('-esal')
    my_dict={'employee':employee}
    return render(request,'testApp/index.html',my_dict)
