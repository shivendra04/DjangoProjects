class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This line is printing at the pre-processing of request')
        response=self.get_response(request)
        print('This line printed at post-processing of request..')
        return response

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>Currently Application Under Maintenance, Please Try After 2 Days!!!! </h1>')


class ExceptionMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response


    def process_exception(self,request,exception):
        s1='<h1>Currently we are facing some technical problems. Please try after some times!!</h1><hr>'
        s2='<h2>Raised Exception: {}</h2>'.format(exception.__class__.__name__)
        s3='<h2>Exception Description/Message: {}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printing  by first middleware at the pre-processing of request')
        response=self.get_response(request)
        print('This line printed by first middleware at  post-processing of request..')
        return response


class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printing  by second middleware at the pre-processing of request')
        response=self.get_response(request)
        print('This line printed by second middleware at  post-processing of request..')
        return response



class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This line is printing  by third middleware at the pre-processing of request')
        response=self.get_response(request)
        print('This line printed by third middleware at  post-processing of request..')
        return response
