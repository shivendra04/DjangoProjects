from django.shortcuts import render
from testApp.forms import AddItemForm
# Create your views here.
def add_item_view(request):
    form=AddItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(30)# after 30sec data will go if no activity
    return render(request,'testApp/additem.html',{'form':form})

def display_item_view(request):
    return render(request,'testApp/displayitems.html')

'''
this view added to get session info
def session_info_view(request):
    session=request.session
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print('Age',age)
    print('Date',date)
    return render(request,'testApp/additem.html')
'''
