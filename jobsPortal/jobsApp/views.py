from django.shortcuts import render
from jobsApp.models import hydjobs,punejobs,chennaijobs,banglorejobs

#emp_list=Employee.objects.all()
# Create your views here.
def home(request):
    return render(request,'jobsPortal/index.html')

def hydjob(request):
    hydjobs_list=hydjobs.objects.all()
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'jobsPortal/hydjobs.html',context=my_dict)

def punejob(request):
    punejobs_list=punejobs.objects.all()
    my_dict={'punejobs_list':punejobs_list}
    return render(request,'jobsPortal/punejobs.html',context=my_dict)
def banglorejob(request):
    bnglrjobs_list=banglorejobs.objects.all()
    my_dict={'bnglrjobs_list':bnglrjobs_list}
    return render(request,'jobsPortal/banglorejobs.html',context=my_dict)
def chennaijob(request):
    chennaijobs_list=chennaijobs.objects.all()
    my_dict={'chennaijobs_list':chennaijobs_list}
    return render(request,'jobsPortal/chennaijobs.html',context=my_dict)
