from django.shortcuts import render,redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm

# Create your views here.
def retriev_view(request):
    employees=Employee.objects.all()
    return render(request,'testApp/index.html',{'employees':employees})
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'testApp/create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/index')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'testApp/update.html',{'employee':employee})
