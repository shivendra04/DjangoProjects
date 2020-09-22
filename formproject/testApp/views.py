from django.shortcuts import render
from . import forms
#. for current working directory
# Create your views here.
def StudentRegister(request):
    form=forms.StudentRegistration()
    return render(request,'testApp/register.html',{'form':form})
