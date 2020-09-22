from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')
def moviesInfo(request):
    head_msg='Latest Movies'
    msg1='Hare Krishna'
    msg2='Jai Jagannath'
    msg3='Chaitanya'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsInfo(request):
    head_msg='Latest Sports News'
    msg1='Hare Krishna School'
    msg2='Jagannath Festival'
    msg3='Chida dahi festival'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
def politicsInfo(request):
    head_msg='Latest Potitics News'
    msg1='Hare Krishna Dancing'
    msg2='Jagannath RathYatra'
    msg3='Karthik Yatra'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
