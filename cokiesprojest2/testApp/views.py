from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testApp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request, 'testApp/age.html')
    response.set_cookie('name',name)
    return response

def result_view(request):
    age=request.GET['age']
    name=request.COOKIES.get('name')
    response=render(request, 'testApp/result.html',{'name':name,'age':age})
    return response
