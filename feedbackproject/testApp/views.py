from django.shortcuts import render
from . import forms

# Create your views here.
def thankyou_view(request):
    return render(request,'testApp/thankyou.html')

def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedBackForm()

    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback info..')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Rollno:',form.cleaned_data['rollno'])
            print('Student Mail ID:',form.cleaned_data['email'])
            print('Student Feedbak',form.cleaned_data['feedback'])
            return thankyou_view(request)
    return render(request,'testApp/feedback.html',{'form':form})
