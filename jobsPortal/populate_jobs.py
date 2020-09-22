import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsPortal.settings')
import django
django.setup()


from jobsApp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7, 9)
    num=''+str(d1)
    for i in range(0,9):
        num=num+str(randint(0, 9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Lead','Team Lead','Softwere Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,
        title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

        punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,
        title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

        chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,
        title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

        banglorejobs_record=banglorejobs.objects.get_or_create(date=fdate,company=fcompany,
        title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)


populate(25)
