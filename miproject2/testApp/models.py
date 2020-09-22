from django.db import models

# Create your models here.

class contactinfo(models.Model):
	Name=models.CharField(max_length=64)
	email=models.EmailField()
	address=models.CharField(max_length=64)
	class Meta:
		abstract=True

class student(contactinfo):
	rollno=models.IntegerField()
	marks=models.IntegerField()

class teacher(contactinfo):
	subject=models.CharField(max_length=64)
	salary=models.IntegerField()


class contactinfo1(models.Model):
	Name=models.CharField(max_length=64)
	email=models.EmailField()
	address=models.CharField(max_length=64)

class student1(contactinfo):
	rollno=models.IntegerField()
	marks=models.IntegerField()

class teacher1(contactinfo):
	subject=models.CharField(max_length=64)
	salary=models.IntegerField()
